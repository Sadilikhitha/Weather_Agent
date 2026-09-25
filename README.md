# 🌦️ SkyCast Weather Agent
AI-Powered Weather Intelligence & Conversational Assistant

<p> Real-time weather data  • Generative AI  • Smart recommendations  • Modern UI </p>
<br>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white"> <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white"> <img src="https://img.shields.io/badge/REST%20API-FF6F00?style=for-the-badge">

</div>

A lightweight weather assistant that combines **live weather data with Google Gemini** to answer weather-related questions in a conversational way.

The agent does not rely on the language model alone. Weather information is fetched from `wttr.in`, passed to the model as context, and used to generate practical responses.

---

## Overview

The Weather Agent is the AI layer behind **SkyCast Weather AI**.

Its main responsibility is to take:

* the user's question
* current weather data
* recent conversation history

and produce a short, weather-specific response.

For example:

```text
Weather:
Hyderabad — 29°C, Overcast, Feels like 31°C

User:
Is it too hot for a run?

SkyCast:
It's fairly warm for running. Stay hydrated and
consider running during a cooler part of the day.
```

The frontend sends the current weather and conversation history to the FastAPI backend, which passes them to the weather agent.

---

## Tech Stack

| Component           | Technology              |
| ------------------- | ----------------------- |
| Language            | Python                  |
| AI Model            | Google Gemini 2.5 Flash |
| AI Integration      | LangChain Google GenAI  |
| Weather Source      | wttr.in                 |
| HTTP Client         | Requests                |
| Configuration       | python-dotenv           |
| Backend Integration | FastAPI                 |
| Data Format         | JSON                    |

The Gemini model is configured with a low temperature (`0.3`) to keep responses relatively focused and consistent.

---

## How It Works

```text
                 USER QUESTION
                       │
                       ▼
              ┌─────────────────┐
              │  FastAPI /ask   │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
     User Query   Live Weather   Chat History
                       │            │
                       └─────┬──────┘
                             ▼
                    ┌─────────────────┐
                    │  Context Builder│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Gemini 2.5     │
                    │     Flash       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Response Cleaner│
                    └────────┬────────┘
                             │
                             ▼
                      AI RESPONSE
```
<img width="657" height="937" alt="image" src="https://github.com/user-attachments/assets/e48436d6-2104-464d-bbc7-1066bf6d6e04" />

## Core Agent Flow

The agent follows a simple sequence:

### 1. Get Live Weather

Weather data is retrieved from:

```text
https://wttr.in/{city}?format=j1
```

The current conditions are converted into a smaller structured object containing values such as:

* Temperature
* Feels-like temperature
* Weather condition
* Humidity
* Wind speed
* Wind direction
* Pressure
* Visibility
* UV index
* Precipitation

---

### 2. Build Weather Context

The retrieved weather data is converted into JSON before being included in the Gemini prompt.

```python
weather_context = json.dumps(
    weather_data,
    ensure_ascii=False,
    indent=2
)
```

This gives the model a clearly structured representation of the current weather instead of asking it to infer conditions from the user's question.

---

### 3. Add Conversation Context

The agent supports follow-up questions.

For example:

```text
User:
What is the temperature?

SkyCast:
It is 29°C.

User:
Is it good for running?

SkyCast:
It's fairly warm, so stay hydrated...
```

The latest **12 messages** are retained and included in the prompt. This is intentionally limited to control token usage.

The frontend also clears the conversation history when the user changes location so that weather information from the previous city is not reused.

---

## System Prompt Design

The agent has a dedicated system prompt defining how it should use weather information.

Important rules include:

* Use supplied live weather data when available.
* Remember recent conversation context.
* Do not ask for the city again when it is already present.
* Do not invent weather information.
* Keep responses concise.
* Distinguish weather facts from recommendations.

This is important because the model is not simply being asked:

```text
"Answer this weather question."
```

Instead, it receives both **rules and current weather context**.

---

## Practical Recommendation Logic

The system prompt also defines how weather conditions should translate into practical suggestions.

### 🌡️ Hot Weather

The agent can recommend:

* Hydration
* Light or breathable clothing
* Sun protection

### ☀️ High UV

The agent can recommend:

* Sunscreen
* Sunglasses
* Limiting prolonged direct sunlight

### 🌧️ High Rain Probability

The agent can recommend:

* Carrying an umbrella
* Rain protection

### 💨 Strong Wind

The response can mention:

* The effect of wind on perceived temperature
* Outdoor activity considerations

### 🌫️ Poor Visibility

The agent can mention:

* Travel caution

### ❄️ Cold Weather

The agent can recommend:

* Appropriate warm clothing

---

## Context-Aware Follow-Up Questions

One of the useful parts of the implementation is that the user does not have to repeat the location.

For example:

```text
User:
Will it rain today?

SkyCast:
There is a chance of rain today.

User:
Should I carry an umbrella?

SkyCast:
Yes, carrying an umbrella would be useful.

User:
What should I wear?

SkyCast:
Light, breathable clothing would be comfortable.
```

The agent explicitly handles these as follow-up questions using the existing weather context.

---

## Prompt Construction

The final prompt is assembled from four main parts:

```text
SYSTEM INSTRUCTIONS
        +
LIVE WEATHER DATA
        +
RECENT CONVERSATION
        +
LATEST USER QUESTION
        ↓
     GEMINI
        ↓
   FINAL ANSWER
```

This structure is implemented in `ask_weather_agent()`.

---

## Response Handling

Gemini responses may not always arrive as a simple string.

The project includes a `clean_response()` function that handles:

* String responses
* Lists
* Dictionaries
* Nested text/content fields

The function converts these formats into a clean string before returning the answer to the API.

This keeps the FastAPI response format simple:

```json
{
  "answer": "It's fairly warm for running. Stay hydrated..."
}
```

---

## Weather Forecast Support

The weather module also processes forecast information.

It reads up to **five forecast days** and extracts:

* Date
* Maximum temperature
* Minimum temperature
* Condition
* Rain probability

For each day, the implementation uses an available hourly forecast entry when present.

The resulting response contains both current weather information and a `forecast` list.

---

## FastAPI Integration

The weather agent is exposed through the FastAPI backend.

### `GET /weather`

Used by the frontend to retrieve weather information for a selected city.

```text
GET /weather?city=Hyderabad
```

The endpoint calls:

```python
get_weather_data(city)
```

and returns the resulting weather information.

### `POST /ask`

Used for conversational weather questions.

The request contains:

```json
{
  "question": "Is it too hot for a run?",
  "weather_data": {},
  "chat_history": []
}
```

The backend passes these values to:

```python
ask_weather_agent(
    user_query=question,
    weather_data=weather_data,
    chat_history=chat_history
)
```

and returns:

```json
{
  "answer": "..."
}
```

---

## Frontend → Backend → AI Flow

The frontend sends the current weather and chat history along with the user's question.

```text
Browser
   │
   │ POST /ask
   ▼
FastAPI
   │
   ├── User Question
   ├── Current Weather
   └── Chat History
          │
          ▼
   Weather Agent
          │
          ▼
   Gemini 2.5 Flash
          │
          ▼
      AI Answer
          │
          ▼
       Browser
```

This integration is implemented in the frontend JavaScript using `fetch()` and JSON.

---

## Environment Setup

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

The application loads environment variables using `python-dotenv`.

### Install Dependencies

```bash
pip install fastapi uvicorn requests python-dotenv langchain-google-genai
```

### Run the Backend

```bash
uvicorn backend.main:app --reload
```

The FastAPI application is initialized with the name **SkyCast Weather AI**.

---

## Project Structure

```text
SkyCast/
│
├── backend/
│   ├── main.py
│   └── weather_agent.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .env
├── requirements.txt
└── README.md
```

---

## Key Implementation Decisions

### Live data is passed to the model

The agent does not ask Gemini to guess current weather conditions. Weather data is retrieved separately and explicitly supplied as context.

### Conversation history is limited

Only the latest 12 messages are retained. This keeps the prompt smaller while still supporting follow-up questions.

### Location changes reset conversation

When the user changes cities, the frontend clears the previous conversation. This prevents old location context from being carried into the new session.

### Weather facts and advice are separated

The system prompt explicitly tells the model to distinguish factual weather values from recommendations.

### API failures are handled

## Both the weather service and Gemini calls have exception handling so failures can be surfaced to the FastAPI layer instead of silently returning incorrect information.

## What This Demonstrates

From a development perspective, this project demonstrates:

* Integrating a **Generative AI model into a real application**
* Using an external API as a source of live data
* Building prompts with structured context
* Maintaining limited conversational memory
* Connecting a JavaScript frontend to a Python backend
* Designing REST endpoints with FastAPI
* Handling external API and model errors
* Using environment variables for API credentials
* Converting model output into a consistent API response

---

## Limitations

* Weather data depends on the availability of `wttr.in`.
* AI responses depend on Google Gemini API availability and quota.
* Conversation history is maintained in the client session rather than a persistent database.
* The current implementation does not provide long-term user memory.
* The backend currently accepts CORS requests from all origins, which should be restricted before production deployment. The current FastAPI configuration uses `allow_origins=["*"]`.

---

## Future Improvements

* Add persistent conversation storage.
* Add authentication and user sessions.
* Restrict CORS to the deployed frontend domain.
* Add request validation using Pydantic models.
* Add API-level rate limiting and caching.
* Add structured logging.
* Add automated tests for weather and agent functions.
* Add fallback weather providers.
* Improve forecast-specific question handling.

---

## 👩‍💻 Project

**SkyCast Weather AI**

A weather application combining:

```text
🌦️ Live Weather Data
        +
🤖 Google Gemini
        +
🔗 LangChain
        +
🐍 Python / FastAPI
        +
💻 JavaScript Frontend
        ↓
Conversational Weather Assistance
```

**Built as a practical Generative AI application rather than a standalone chatbot.**
