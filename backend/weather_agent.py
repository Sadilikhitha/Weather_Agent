from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

import requests
import os
import json


# =========================================================
# ENV
# =========================================================

load_dotenv()


# =========================================================
# GEMINI
# =========================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)


# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are SkyCast, a friendly AI weather assistant.

You help the user understand their current weather and
give practical weather-related recommendations.

You have access to LIVE weather data from the user's
SkyCast dashboard.

IMPORTANT:

1. Always use the supplied live weather data when it is
   available.

2. The user may ask follow-up questions without repeating
   their city.

3. Remember the context of the recent conversation.

4. Never ask for the city again if the weather data already
   contains the city.

5. Do not invent weather information.

6. Keep answers concise and conversational.

You can help with:

- current weather
- temperature
- feels-like temperature
- rain
- umbrella
- what to wear
- what to carry
- sunscreen
- sunglasses
- hydration
- outdoor activities
- running
- walking
- travel
- UV
- humidity
- wind
- visibility
- today's weather
- upcoming forecast
- morning weather
- afternoon weather
- evening weather
- weather safety

Practical advice:

If it is hot:
- recommend hydration
- suggest light/breathable clothing
- consider sun protection

If UV is high:
- recommend sunscreen
- recommend sunglasses
- recommend limiting prolonged direct sun exposure

If rain probability is high:
- recommend an umbrella or rain protection

If wind is strong:
- mention that it may feel cooler
- mention outdoor activity considerations

If visibility is poor:
- mention travel caution

If it is cold:
- recommend appropriate warm clothing

IMPORTANT:
Distinguish between weather facts and recommendations.

Example:

Weather:
"Chennai is 31°C with 66% humidity."

Advice:
"Light, breathable clothing would be comfortable."

Do not claim that you personally observed the weather.

If the question is unrelated to weather, politely explain
that you specialize in weather assistance.
"""


# =========================================================
# WEATHER TOOL
# =========================================================

def get_weather(city: str):

    url = f"https://wttr.in/{city}?format=j1"

    try:

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code != 200:

            return {
                "error": "Weather service unavailable."
            }

        data = response.json()

        current = data["current_condition"][0]

        return {
            "city": city,
            "temperature": current["temp_C"],
            "feels_like": current["FeelsLikeC"],
            "condition": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "wind_speed": current["windspeedKmph"],
            "wind_direction": current["winddir16Point"],
            "pressure": current["pressure"],
            "visibility": current["visibility"],
            "uv_index": current["uvIndex"],
            "precipitation": current["precipMM"],
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# =========================================================
# RESPONSE CLEANER
# =========================================================

def clean_response(content):

    if isinstance(content, str):
        return content.strip()


    if isinstance(content, list):

        parts = []

        for item in content:

            if isinstance(item, str):

                parts.append(item)

            elif isinstance(item, dict):

                if "text" in item:

                    parts.append(
                        str(item["text"])
                    )

                elif "content" in item:

                    parts.append(
                        str(item["content"])
                    )


        return "\n".join(parts).strip()


    if isinstance(content, dict):

        if "text" in content:

            return str(
                content["text"]
            ).strip()


        if "content" in content:

            return str(
                content["content"]
            ).strip()


    return str(content).strip()


# =========================================================
# ASK SKYCAST
# =========================================================

def ask_weather_agent(
    user_query: str,
    weather_data: dict | None = None,
    chat_history: list | None = None
):

    if chat_history is None:

        chat_history = []


    # =====================================================
    # LIMIT HISTORY
    # =====================================================

    # Only use the latest 12 messages.
    # This keeps token usage under control.

    chat_history = chat_history[-12:]


    # =====================================================
    # WEATHER CONTEXT
    # =====================================================

    if weather_data:

        weather_context = json.dumps(
            weather_data,
            ensure_ascii=False,
            indent=2
        )

    else:

        weather_context = (
            "No live dashboard weather data is available."
        )


    # =====================================================
    # CONVERSATION CONTEXT
    # =====================================================

    history_text = ""

    for message in chat_history:

        role = message.get("role")

        content = message.get("content")


        if not content:
            continue


        if role == "user":

            history_text += (
                f"User: {content}\n"
            )


        elif role == "assistant":

            history_text += (
                f"SkyCast: {content}\n"
            )


    # =====================================================
    # FINAL PROMPT
    # =====================================================

    prompt = f"""
{SYSTEM_PROMPT}

==================================================
LIVE WEATHER DATA
==================================================

{weather_context}

==================================================
RECENT CONVERSATION
==================================================

{history_text}

==================================================
LATEST USER QUESTION
==================================================

{user_query}

==================================================
INSTRUCTIONS
==================================================

Answer the latest user question.

Use the live weather data above.

Remember the previous conversation.

If the user says:

"what should I wear?"

"what should I carry?"

"should I take an umbrella?"

"what about sunscreen?"

"what about sunglasses?"

"can I go for a run?"

understand that these are follow-up questions about the
current location.

Do NOT ask for the city again when the live weather data
already contains the city.

Give practical advice based on the actual weather values.

Keep the response short, natural, and useful.
"""


    # =====================================================
    # CALL GEMINI
    # =====================================================

    try:

        result = llm.invoke(
            prompt
        )


        answer = clean_response(
            result.content
        )


        if not answer:

            return (
                "I couldn't generate a response. "
                "Please try again."
            )


        return answer


    except Exception as e:

        print(
            "GEMINI ERROR:",
            repr(e)
        )

        raise Exception(
            f"Gemini error: {str(e)}"
        )


# =========================================================
# DASHBOARD WEATHER
# =========================================================

def get_weather_data(city: str):

    city = city.strip()


    if not city:

        raise Exception(
            "City is required"
        )


    url = (
        f"https://wttr.in/"
        f"{city}"
        f"?format=j1"
    )


    try:

        response = requests.get(
            url,
            timeout=10
        )


        if response.status_code != 200:

            raise Exception(
                "Weather service unavailable"
            )


        data = response.json()


        current = (
            data["current_condition"][0]
        )


        forecast = data.get(
            "weather",
            []
        )


        forecast_data = []


        for day in forecast[:5]:

            hourly = day.get(
                "hourly",
                []
            )


            # Use a middle forecast period
            # when available.
            if hourly:

                hour_data = hourly[
                    min(4, len(hourly) - 1)
                ]

                condition = (
                    hour_data
                    .get(
                        "weatherDesc",
                        [{"value": "Unknown"}]
                    )[0]
                    .get(
                        "value",
                        "Unknown"
                    )
                )

                rain_chance = (
                    hour_data.get(
                        "chanceofrain",
                        "0"
                    )
                )

            else:

                condition = "Unknown"
                rain_chance = "0"


            forecast_data.append({

                "date":
                    day.get(
                        "date",
                        ""
                    ),

                "max_temp":
                    day.get(
                        "maxtempC",
                        ""
                    ),

                "min_temp":
                    day.get(
                        "mintempC",
                        ""
                    ),

                "condition":
                    condition,

                "rain_chance":
                    rain_chance

            })


        return {

            "city": city,

            "temperature":
                current.get(
                    "temp_C",
                    ""
                ),

            "feels_like":
                current.get(
                    "FeelsLikeC",
                    ""
                ),

            "condition":
                current.get(
                    "weatherDesc",
                    [{"value": ""}]
                )[0].get(
                    "value",
                    ""
                ),

            "humidity":
                current.get(
                    "humidity",
                    ""
                ),

            "wind_speed":
                current.get(
                    "windspeedKmph",
                    ""
                ),

            "wind_direction":
                current.get(
                    "winddir16Point",
                    ""
                ),

            "pressure":
                current.get(
                    "pressure",
                    ""
                ),

            "visibility":
                current.get(
                    "visibility",
                    ""
                ),

            "uv_index":
                current.get(
                    "uvIndex",
                    ""
                ),

            "precipitation":
                current.get(
                    "precipMM",
                    ""
                ),

            "forecast":
                forecast_data

        }


    except requests.RequestException as e:

        raise Exception(
            f"Weather service error: {str(e)}"
        )


    except Exception as e:

        raise Exception(
            f"Could not get weather data: {str(e)}"
        )