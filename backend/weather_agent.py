from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

import requests
import os
import json
import re
import datetime


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
You are SkyCast, a friendly professional weather and trip intelligence assistant.

==================================================
NORMAL CONVERSATION
==================================================

Not every message is a weather question.

If the user says:

- hi
- hello
- hey
- hey hi
- good morning
- good evening
- how are you
- thanks
- thank you

DO NOT fetch weather.

DO NOT ask for a destination.

DO NOT give trip information.

Simply respond naturally and briefly.

Examples:

User: Hey hi!
Assistant: Hello! How can I help you today?

User: Hi
Assistant: Hi! How can I help you?

User: Good morning
Assistant: Good morning! How can I help you today?


==================================================
TRIP / WEATHER QUESTIONS
==================================================

Only use weather intelligence when the user actually asks about:

- a trip
- travelling
- visiting a place
- a destination
- weather
- forecast
- what to carry
- what to wear
- whether they can travel
- outdoor activities
- travel conditions


==================================================
TRIP INTELLIGENCE
==================================================

When a destination is mentioned:

1. Identify the destination.
2. Identify the trip duration if provided.
3. Use the destination's 5-day forecast.
4. Analyze the forecast across those days.
5. Answer the user's actual question.
6. Give practical recommendations based on the forecast.
7. Mention specific dates when weather conditions matter.
8. Do not give generic advice that is not supported by the forecast.
9. Do not dump raw weather data.
10. Keep the answer concise.


==================================================
IMPORTANT
==================================================

The 5-day forecast is the basis for your recommendations.

For example:

If rain is expected on one day:

"The trip looks suitable overall. However, light rain is expected
on 26 September, so carry an umbrella or light raincoat."

If temperatures are very high:

"Temperatures will be high, so carry sunscreen, sunglasses and water."

If weather is comfortable:

"The weather looks comfortable for travelling and sightseeing."

If strong rain or bad weather is expected:

"Weather may affect outdoor activities on that day, so keep your
plans flexible."

DO NOT recommend an umbrella just because the user is travelling.

DO NOT recommend warm clothes just because it is a trip.

Only recommend items supported by the forecast.


==================================================
ANSWER THE USER'S QUESTION
==================================================

If user asks:

"Can I travel?"

Answer travel suitability first.

If user asks:

"What should I carry?"

Give useful things to carry based on the forecast.

If user asks:

"What should I wear?"

Focus mainly on clothing.

If user asks:

"Which day is better?"

Compare the forecast days and identify the suitable day.

If user asks:

"Will it rain?"

Focus on rain and the dates when rain is expected.


==================================================
FOLLOW-UP QUESTIONS
==================================================

If the user previously mentioned a destination and then asks:

"What should I carry?"

"What should I wear?"

"Should I take an umbrella?"

"What about sunscreen?"

"What about sunglasses?"

"Can I go outside?"

Treat it as a follow-up about the same destination.

Do not ask for the destination again if the conversation already contains it.

Use the available destination forecast.


==================================================
STYLE
==================================================

Be concise.

Be natural.

Be practical.

Do not explain how the AI works.

Do not mention APIs.

Do not mention Gemini.

Do not repeat the same recommendation unnecessarily.

Answer only what the user needs.
"""


# =========================================================
# GREETING DETECTOR
# =========================================================

def is_greeting(user_query: str):

    if not user_query:
        return False

    text = user_query.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "hey hi",
        "hi there",
        "hello there",
        "good morning",
        "good afternoon",
        "good evening",
        "how are you",
        "thanks",
        "thank you"
    ]

    # Remove common punctuation
    cleaned = re.sub(r"[!?.,]+", "", text).strip()

    return cleaned in greetings


# =========================================================
# DESTINATION DETECTOR
# =========================================================

def detect_trip_destination(user_query: str):

    if not user_query:
        return None

    text = user_query.strip()

    patterns = [

        # going to Bangalore
        r"\b(?:going|go|travelling|traveling|visiting|visit)\s+to\s+([A-Za-z][A-Za-z .'-]{1,60}?)(?=\s+(?:for|on|from|between|during|and|what|can|should|will)\b|[?.!,]|$)",

        # trip to Bangalore
        r"\btrip\s+to\s+([A-Za-z][A-Za-z .'-]{1,60}?)(?=\s+(?:for|on|from|between|during|and|what|can|should|will)\b|[?.!,]|$)",

        # weather in Bangalore
        r"\b(?:weather|forecast)\s+(?:in|at|for|of)\s+([A-Za-z][A-Za-z .'-]{1,60}?)(?=\s+(?:for|on|from|between|during|and|what|can|should|will)\b|[?.!,]|$)",

        # Bangalore weather
        r"\b([A-Za-z][A-Za-z .'-]{1,60}?)\s+(?:weather|forecast)\b"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            location = match.group(1).strip()

            if len(location) >= 2:
                return location

    return None

# =========================================================
# TRIP DURATION DETECTOR
# =========================================================

def detect_trip_dates(user_query: str):
    """
    Detect travel date ranges such as:
    30-09 to 3-10
    30/09 to 03/10
    30 September to 3 October
    """

    if not user_query:
        return None

    text = user_query.strip()

    patterns = [
        # 30-09 to 3-10
        r"\b(\d{1,2})[-/](\d{1,2})\s*(?:to|-)\s*(\d{1,2})[-/](\d{1,2})\b",

        # 30 September to 3 October
        r"\b(\d{1,2})\s+([A-Za-z]+)\s*(?:to|-)\s*(\d{1,2})\s+([A-Za-z]+)\b",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(0)

    return None


# =========================================================
# TRIP DAYS DETECTOR
# =========================================================

def detect_trip_days(user_query: str):
    """
    Detect an explicit trip duration such as:
    "for 4 days" or "4 day trip".

    If the user gives a date range such as
    "30-09 to 3-10", calculate the inclusive number of days.
    """
    if not user_query:
        return None

    text = user_query.strip()

    patterns = [
        r"\bfor\s+(\d{1,2})\s+days?\b",
        r"\b(\d{1,2})\s+days?\s+(?:trip|travel|vacation)\b",
        r"\b(\d{1,2})[- ]day\s+(?:trip|travel|vacation)\b",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return int(match.group(1))

    date_match = re.search(
        r"\b(\d{1,2})[-/](\d{1,2})\s*(?:to|-)\s*(\d{1,2})[-/](\d{1,2})\b",
        text,
        re.IGNORECASE,
    )

    if date_match:
        start_day, start_month, end_day, end_month = map(
            int, date_match.groups()
        )
        year = datetime.datetime.now().year

        try:
            start_date = datetime.date(year, start_month, start_day)
            end_date = datetime.date(year, end_month, end_day)

            if end_date < start_date:
                end_date = datetime.date(year + 1, end_month, end_day)

            return (end_date - start_date).days + 1
        except ValueError:
            return None

    return None


# =========================================================
# CONVERSATION CONTEXT
# =========================================================

def get_context_from_history(chat_history: list | None):
    """
    Recover destination, trip duration and trip dates from
    previous USER messages.
    """
    if not chat_history:
        return None, None, None

    destination = None
    trip_days = None
    trip_dates = None

    for message in reversed(chat_history):
        if not isinstance(message, dict):
            continue

        if message.get("role") != "user":
            continue

        content = message.get("content", "")
        if not isinstance(content, str) or not content.strip():
            continue

        if destination is None:
            destination = detect_trip_destination(content)

        if trip_dates is None:
            trip_dates = detect_trip_dates(content)

        if trip_days is None:
            trip_days = detect_trip_days(content)

        if destination and (trip_dates or trip_days):
            break

    return destination, trip_days, trip_dates


# =========================================================
# LOCATION WEATHER
# =========================================================

def get_trip_weather(city: str):

    city = city.strip()

    if not city:
        raise Exception("Destination is required.")

    # -----------------------------------------------------
    # First try Open-Meteo geocoding
    # -----------------------------------------------------

    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

    geocode_response = requests.get(
        geocode_url,
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=10
    )

    if geocode_response.status_code != 200:
        raise Exception("Unable to find the destination.")

    geocode_data = geocode_response.json()

    results = geocode_data.get("results", [])

    if not results:
        raise Exception(
            f"Could not find weather location: {city}"
        )

    location = results[0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    resolved_name = location.get(
        "name",
        city
    )

    country = location.get(
        "country",
        ""
    )

    # -----------------------------------------------------
    # Get 5-day forecast
    # -----------------------------------------------------

    forecast_url = "https://api.open-meteo.com/v1/forecast"

    forecast_response = requests.get(
        forecast_url,
        params={
            "latitude": latitude,
            "longitude": longitude,

            "forecast_days": 5,

            "timezone": "auto",

            "daily": ",".join([
                "weather_code",
                "temperature_2m_max",
                "temperature_2m_min",
                "apparent_temperature_max",
                "apparent_temperature_min",
                "precipitation_probability_max",
                "precipitation_sum",
                "rain_sum",
                "precipitation_hours",
                "uv_index_max",
                "wind_speed_10m_max",
                "wind_gusts_10m_max"
            ])
        },
        timeout=10
    )

    if forecast_response.status_code != 200:
        raise Exception(
            "Weather forecast service unavailable."
        )

    data = forecast_response.json()

    daily = data.get(
        "daily",
        {}
    )

    dates = daily.get("time", [])

    forecast = []

    for i, date in enumerate(dates):

        forecast.append({
            "date": date,

            "max_temperature": daily.get(
                "temperature_2m_max",
                [""] * len(dates)
            )[i],

            "min_temperature": daily.get(
                "temperature_2m_min",
                [""] * len(dates)
            )[i],

            "max_apparent_temperature": daily.get(
                "apparent_temperature_max",
                [""] * len(dates)
            )[i],

            "min_apparent_temperature": daily.get(
                "apparent_temperature_min",
                [""] * len(dates)
            )[i],

            "rain_probability": daily.get(
                "precipitation_probability_max",
                [""] * len(dates)
            )[i],

            "precipitation": daily.get(
                "precipitation_sum",
                [""] * len(dates)
            )[i],

            "rain": daily.get(
                "rain_sum",
                [""] * len(dates)
            )[i],

            "precipitation_hours": daily.get(
                "precipitation_hours",
                [""] * len(dates)
            )[i],

            "uv_index": daily.get(
                "uv_index_max",
                [""] * len(dates)
            )[i],

            "wind_speed": daily.get(
                "wind_speed_10m_max",
                [""] * len(dates)
            )[i],

            "wind_gusts": daily.get(
                "wind_gusts_10m_max",
                [""] * len(dates)
            )[i],

            "weather_code": daily.get(
                "weather_code",
                [""] * len(dates)
            )[i]
        })

    return {
        "destination": resolved_name,
        "country": country,
        "latitude": latitude,
        "longitude": longitude,
        "forecast_days": 5,
        "forecast": forecast
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

    # Keep latest 12 messages
    chat_history = chat_history[-12:]


    # =====================================================
    # GREETING
    # =====================================================

    if is_greeting(user_query):

        return "Hello! How can I help you today?"


    # =====================================================
    # DETECT INFORMATION FROM CURRENT MESSAGE
    # =====================================================

    trip_destination = detect_trip_destination(
        user_query
    )

    trip_days = detect_trip_days(
        user_query
    )

    trip_dates = detect_trip_dates(
        user_query
    )


    # =====================================================
    # RECOVER INFORMATION FROM PREVIOUS MESSAGES
    # =====================================================

    history_destination, history_days, history_dates = (
        get_context_from_history(
            chat_history
        )
    )


    # Use current message first.
    # If missing, use previous conversation.

    if not trip_destination:
        trip_destination = history_destination

    if not trip_days:
        trip_days = history_days

    if not trip_dates:
        trip_dates = history_dates


    # =====================================================
    # GET 5-DAY DESTINATION FORECAST
    # =====================================================

    destination_weather = None

    if trip_destination:

        try:

            destination_weather = get_trip_weather(
                trip_destination
            )

            print(
                "DESTINATION:",
                trip_destination
            )

            print(
                "TRIP DAYS:",
                trip_days
            )

            print(
                "TRIP DATES:",
                trip_dates
            )

        except Exception as e:

            print(
                "TRIP WEATHER ERROR:",
                repr(e)
            )


    # =====================================================
    # WEATHER CONTEXT
    # =====================================================

    weather_context_parts = []


    # Dashboard weather
    if weather_data:

        weather_context_parts.append(
            "CURRENT DASHBOARD WEATHER:\n"
            +
            json.dumps(
                weather_data,
                ensure_ascii=False,
                indent=2
            )
        )


    # Destination 5-day forecast
    if destination_weather:

        weather_context_parts.append(
            "DESTINATION 5-DAY FORECAST:\n"
            +
            json.dumps(
                destination_weather,
                ensure_ascii=False,
                indent=2
            )
        )


    if weather_context_parts:

        weather_context = "\n\n".join(
            weather_context_parts
        )

    else:

        weather_context = (
            "No weather data is available."
        )


    # =====================================================
    # CONVERSATION HISTORY
    # =====================================================

    history_text = ""

    for message in chat_history:

        role = message.get(
            "role"
        )

        content = message.get(
            "content"
        )

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
PREVIOUS CONVERSATION
==================================================

{history_text}


==================================================
TRIP CONTEXT
==================================================

Destination:
{trip_destination or "Not specified"}

Trip duration:
{trip_days or "Not specified"}

Trip dates:
{trip_dates or "Not specified"}


==================================================
LATEST USER QUESTION
==================================================

{user_query}


==================================================
IMPORTANT INSTRUCTIONS
==================================================

The user may provide trip information across
multiple messages.

For example:

User:
"I am going to Bangalore for a trip."

User:
"from 30-09 to 3-10"

User:
"give"

You MUST combine those messages.

Destination = Bangalore
Dates = 30-09 to 3-10

Do NOT ask the user for the destination again.

Do NOT ask the user for the dates again.

Use the destination's 5-day forecast.

Analyze the forecast for the user's trip period.

If rain is expected on a specific date,
mention that date.

If the weather is suitable:
say that the trip looks suitable.

If rain is expected:
recommend an umbrella/raincoat only when appropriate.

If it is hot:
recommend sunscreen, sunglasses, water, light clothing, etc.

If it is cold:
recommend appropriate warm clothing.

If wind is strong:
mention it when relevant.

Do NOT give a generic packing list.

Do NOT dump raw weather data.

Answer ONLY what the user asked.

Keep the answer short, natural and practical.
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
        raise Exception("City is required")

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

        current = data["current_condition"][0]

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

            if hourly:

                hour_data = hourly[
                    min(
                        4,
                        len(hourly) - 1
                    )
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