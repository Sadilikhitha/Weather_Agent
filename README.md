<div align="center">

# 🌦️ SkyCast Weather AI

### **AI-Powered Weather Intelligence & Conversational Assistant**

<p>
Real-time weather data &nbsp;•&nbsp; Generative AI &nbsp;•&nbsp; Smart recommendations &nbsp;•&nbsp; Modern UI
</p>

<br>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=111827" alt="JavaScript"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>

<br><br>

<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Uvicorn-2E7D32?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Uvicorn"/>
<img src="https://img.shields.io/badge/LangChain-1F2937?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain"/>
<img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini"/>

<br><br>

<img src="https://img.shields.io/badge/REST_API-0EA5E9?style=for-the-badge" alt="REST API"/>
<img src="https://img.shields.io/badge/Weather_API-38BDF8?style=for-the-badge" alt="Weather API"/>
<img src="https://img.shields.io/badge/Generative_AI-8B5CF6?style=for-the-badge" alt="Generative AI"/>
<img src="https://img.shields.io/badge/Responsive_UI-22C55E?style=for-the-badge" alt="Responsive UI"/>

<br><br>

**☀️ Live Weather   |   🤖 AI Assistance   |   🌧️ Smart Recommendations**

</div>

---

## 🌤️ About SkyCast

**SkyCast** is an AI-powered weather intelligence platform that combines **real-time weather information with Generative AI** to provide conversational, context-aware weather assistance.

Unlike traditional weather applications that only display numerical weather information, SkyCast allows users to interact with weather data using natural language.

### 💬 Example Questions

> ☀️ **"Is it too hot for a run?"**

> ☔ **"Should I carry an umbrella?"**

> 👕 **"What should I wear today?"**

> 🌧️ **"Will it rain today?"**

The application retrieves live weather information, provides the relevant weather context to an AI-powered weather agent, and generates practical recommendations based on the current conditions.

---

## 🛠️ Technology Stack

<div align="center">

|           Layer          | Technologies                                             |
| :----------------------: | :------------------------------------------------------- |
|      🎨 **Frontend**     | HTML5 • CSS3 • JavaScript                                |
|      🐍 **Backend**      | Python • FastAPI • Uvicorn                               |
|   🤖 **Generative AI**   | Google Gemini 2.5 Flash                                  |
|    🔗 **AI Framework**   | LangChain • LangChain Google GenAI                       |
|   🌦️ **Weather Data**   | wttr.in Weather API                                      |
| 📍 **Location Services** | Browser Geolocation API • BigDataCloud Reverse Geocoding |
|   🔌 **Communication**   | REST API • Fetch API                                     |
|   🔐 **Configuration**   | Python-dotenv • Environment Variables                    |
|      📱 **UI / UX**      | Responsive Web Design • Dark/Light Theme                 |
|     🧠 **AI Context**    | Live Weather Context • Conversation History              |

</div>

---

## ✨ Key Features

### 🌍 Live Weather Intelligence

SkyCast retrieves and displays real-time weather information including:

| Weather Metric      | Description                  |
| :------------------ | :--------------------------- |
| 🌡️ **Temperature** | Current temperature          |
| 🤗 **Feels Like**   | Perceived temperature        |
| ☁️ **Condition**    | Current weather condition    |
| 💧 **Humidity**     | Current humidity level       |
| 💨 **Wind**         | Wind speed                   |
| 🌧️ **Rain**        | Rain probability             |
| ☀️ **UV Index**     | UV exposure level            |
| 👁️ **Visibility**  | Visibility distance          |
| 🎚️ **Pressure**    | Atmospheric pressure         |
| 📅 **Forecast**     | Upcoming weather information |

---

### 🤖 Conversational AI Weather Assistant

SkyCast allows users to communicate naturally with the weather assistant instead of manually interpreting weather values.

The AI assistant can help with:

* 🌧️ Rain predictions
* ☔ Umbrella recommendations
* 👕 Clothing suggestions
* 🏃 Running conditions
* 🚶 Walking conditions
* 🌳 Outdoor activities
* 🧴 Sunscreen recommendations
* 🕶️ Sunglasses
* 💧 Hydration
* 💨 Wind conditions
* 👁️ Visibility
* ✈️ Travel considerations
* ⚠️ Weather safety

---

### 📍 My Location

SkyCast supports browser-based location detection.

```text
📍 Browser Location
        │
        ▼
🌐 Latitude + Longitude
        │
        ▼
🔎 Reverse Geocoding
        │
        ▼
🏙️ City Detection
        │
        ▼
🌦️ Live Weather
```

---

### 💬 Context-Aware Conversations

SkyCast maintains recent conversation history so users can ask follow-up questions without repeatedly mentioning their location.

```text
👤 User:
Is it going to rain today?

🤖 SkyCast:
There is a chance of rain today.

👤 User:
Should I carry an umbrella?

🤖 SkyCast:
Yes, carrying an umbrella would be useful.
```

---

### 🎨 Modern Weather-Themed Interface

The frontend provides:

* 🌙 Dark mode
* ☀️ Light mode
* 🌈 Weather-aware visual styling
* 💬 Conversational chat interface
* ⚡ Quick weather prompts
* 📱 Responsive design
* ✨ Modern glass-style dashboard
* 🧭 Location-based weather search

---

## 🏗️ System Architecture

```text
                         👤 USER
                           │
                           ▼
              ┌────────────────────────┐
              │    SKYCAST FRONTEND    │
              │                        │
              │    HTML • CSS • JS     │
              └───────────┬────────────┘
                          │
                          │ REST API
                          ▼
              ┌────────────────────────┐
              │     FASTAPI SERVER     │
              │        Python          │
              └───────────┬────────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
     ┌─────────────────┐    ┌──────────────────┐
     │   🌦️ wttr.in    │    │  🤖 Weather Agent │
     │   Weather API   │    │     LangChain     │
     └────────┬────────┘    └─────────┬────────┘
              │                       │
              │                       ▼
              │              ┌──────────────────┐
              │              │  Google Gemini   │
              │              │    2.5 Flash     │
              │              └─────────┬────────┘
              │                        │
              └────────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │ 🌦️ Weather Intelligence │
                └──────────┬───────────┘
                           │
                           ▼
                    💬 AI Response
```

---

## 🔄 How SkyCast Works

### 01 — 📍 Select Location

The user searches for a city or selects **My Location**.

### 02 — 🌦️ Retrieve Weather

The FastAPI backend requests current weather information from the weather service.

### 03 — 🧠 Prepare Context

The application combines:

```text
🌦️ Live Weather Data
          +
💬 Recent Conversation
          +
❓ User Question
```

### 04 — 🤖 AI Processing

The weather context is passed to **Google Gemini** through the LangChain Google GenAI integration.

### 05 — 💡 Generate Recommendation

Gemini interprets the supplied weather conditions and generates a concise, practical response.

### 06 — 💬 Display Result

The generated response is displayed inside the SkyCast conversational interface.

---

## 📂 Project Structure

```text
SkyCast/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── backend/
│   ├── main.py
│   └── weather_agent.py
│
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧰 Core Technologies

### 🌐 HTML5

Used to build the structure of the SkyCast dashboard, weather cards, navigation controls, quick prompts, and conversational interface.

### 🎨 CSS3

Used for:

* Responsive layouts
* Dark/light themes
* Weather cards
* Animations
* Glassmorphism effects
* Chat bubbles
* Responsive mobile design

### ⚡ JavaScript

Handles:

* Weather API requests
* AI chat requests
* Location detection
* Dynamic weather updates
* Chat history
* Quick prompts
* Theme switching
* Error handling

### 🐍 Python

Used as the primary backend programming language for the weather intelligence and API layer.

### 🚀 FastAPI

Provides the REST API layer connecting the frontend with the weather service and AI agent.

### 🔗 LangChain

Used to integrate the Google Gemini model into the weather assistant workflow and provide contextual AI responses.

### ✨ Google Gemini

Provides the Generative AI capability that understands weather-related questions and generates contextual recommendations.

### 🌦️ wttr.in

Provides live weather and forecast information used by the application.

---

## 🔌 API Endpoints

### `GET /`

Checks whether the SkyCast backend is running.

**Response:**

```json
{
  "message": "SkyCast Weather AI API is running"
}
```

---

### `GET /weather`

Retrieves weather information for a city.

**Example:**

```text
GET /weather?city=Hyderabad
```

---

### `POST /ask`

Processes an AI weather question.

**Example Request:**

```json
{
  "question": "Is it too hot for a run?",
  "weather_data": {
    "city": "Hyderabad",
    "temperature": "29",
    "feels_like": "31",
    "condition": "Overcast",
    "humidity": "63",
    "wind_speed": "17"
  },
  "chat_history": []
}
```

**Example Response:**

```json
{
  "answer": "It is fairly warm for running. Stay hydrated and consider running during a cooler part of the day."
}
```

---

## 🔐 Environment Configuration

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 🔒 Security

Never commit API keys to GitHub.

Recommended `.gitignore`:

```gitignore
.env
.venv/
venv/
__pycache__/
*.pyc
```

---

## 🚀 Running the Project

### 01 — Clone Repository

```bash
git clone <your-repository-url>
cd SkyCast
```

### 02 — Create Virtual Environment

```bash
python -m venv .venv
```

### 03 — Activate Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 04 — Install Dependencies

```bash
pip install -r requirements.txt
```

### 05 — Configure Environment Variables

```env
GOOGLE_API_KEY=your_api_key
```

### 06 — Start FastAPI

```bash
uvicorn backend.main:app --reload
```

### 07 — Open the Frontend

Run the frontend using a local development server and open the application in your browser.

---

## 💬 Example User Interaction

### 🌦️ Live Weather Context

```text
📍 Hyderabad

🌡️ Temperature      29°C
☁️ Condition        Overcast
🤗 Feels Like       31°C

💧 Humidity         63%
💨 Wind             17 km/h
🌧️ Rain             13%
☀️ UV               0
👁️ Visibility       10 km
🎚️ Pressure         1004 hPa
```

### 👤 User

```text
Is it too hot for a run?
```

### 🤖 SkyCast

```text
At 29°C with a feels-like temperature of 31°C,
it's fairly warm for running. Stay hydrated and
consider running during a cooler part of the day.
```

---

## 🔮 Future Enhancements

| Feature                      | Description                                     |
| :--------------------------- | :---------------------------------------------- |
| 🌧️ **Precipitation Radar**  | Advanced rain and precipitation visualization   |
| 🗺️ **Weather Maps**         | Interactive weather mapping                     |
| 🌬️ **Air Quality**          | Air-quality monitoring                          |
| 🔔 **Weather Alerts**        | Severe weather notifications                    |
| 📅 **Extended Forecasts**    | More detailed forecast information              |
| 🎙️ **Voice Assistant**      | Voice-based weather interaction                 |
| 📊 **Weather Analytics**     | Historical weather analysis                     |
| 📱 **PWA Support**           | Progressive Web App capabilities                |
| ⚡ **AI Caching**             | Reduce unnecessary AI API calls                 |
| 🌾 **Agricultural Insights** | Weather-based farming recommendations           |
| 🤖 **Specialized Agents**    | Dedicated AI agents for different weather tasks |

---

## 🎯 Project Highlights

<div align="center">

|         🌦️        |         🤖        |       🔗      |      🐍     |       💻      |
| :----------------: | :---------------: | :-----------: | :---------: | :-----------: |
| **Real-Time Data** | **Generative AI** | **LangChain** | **FastAPI** | **Modern UI** |

<br>

### 🌤️ Real-Time Weather

### +

### 🤖 Generative AI

### +

### 🔗 LangChain

### +

### 🐍 FastAPI

### +

### 💻 Modern Web Interface

### =

### ☁️ **SkyCast Weather Intelligence**

</div>

---

## 👩‍💻 Developer

<div align="center">

### **Likhitha Sadi**

**B.Tech — Information Technology**

<br>

**Areas of Interest**

AI • Generative AI • Full-Stack Development • Python • FastAPI • Machine Learning • Web Development

</div>

---

## ⭐ Project

If you find **SkyCast Weather AI** useful or interesting, consider giving the repository a ⭐.

<div align="center">

### 🌦️ **Built with HTML • CSS • JavaScript • Python • FastAPI • LangChain • Google Gemini**

**Making weather information smarter, simpler, and more conversational.**

</div>
