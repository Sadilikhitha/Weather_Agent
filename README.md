# 🌦️ SkyCast Weather AI

### *AI-Powered Weather Intelligence & Conversational Assistant*

<p align="center">

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

</p>

<p align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge\&logo=gunicorn\&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge\&logo=chainlink\&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge\&logo=google\&logoColor=white)

</p>

<p align="center">

![REST API](https://img.shields.io/badge/REST%20API-FF6F00?style=for-the-badge)
![Weather API](https://img.shields.io/badge/Weather%20API-38BDF8?style=for-the-badge)
![Generative AI](https://img.shields.io/badge/Generative%20AI-8B5CF6?style=for-the-badge)
![Responsive UI](https://img.shields.io/badge/Responsive%20UI-22C55E?style=for-the-badge)

</p>

---

## 🌤️ About SkyCast

**SkyCast** is an AI-powered weather intelligence platform that combines **real-time weather information with Generative AI** to provide conversational, context-aware weather assistance.

Instead of simply displaying weather values, SkyCast allows users to ask natural-language questions such as:

> ☀️ *"Is it too hot for a run?"*

> ☔ *"Should I carry an umbrella?"*

> 👕 *"What should I wear today?"*

> 🌧️ *"Will it rain today?"*

The application retrieves live weather information, passes the relevant weather context to an AI-powered weather agent, and generates practical recommendations based on the current conditions.

---

## 🛠️ Technologies & Tools Used

| Category                 | Technologies                                            |
| ------------------------ | ------------------------------------------------------- |
| 🎨 **Frontend**          | HTML5, CSS3, JavaScript                                 |
| 🐍 **Backend**           | Python, FastAPI, Uvicorn                                |
| 🤖 **Generative AI**     | Google Gemini 2.5 Flash                                 |
| 🔗 **AI Framework**      | LangChain, LangChain Google GenAI                       |
| 🌦️ **Weather Data**     | wttr.in Weather API                                     |
| 📍 **Location Services** | Browser Geolocation API, BigDataCloud Reverse Geocoding |
| 🔌 **API Communication** | REST API, Fetch API                                     |
| 🔐 **Configuration**     | Python-dotenv, Environment Variables                    |
| 📱 **UI**                | Responsive Web Design, Dark/Light Theme                 |
| 🧠 **AI Context**        | Live Weather Context + Conversation History             |

---

## ✨ Key Features

### 🌍 Live Weather Intelligence

SkyCast retrieves and displays real-time weather information including:

* 🌡️ Temperature
* 🤗 Feels-like temperature
* ☁️ Current weather condition
* 💧 Humidity
* 💨 Wind speed
* 🌧️ Rain probability
* ☀️ UV index
* 👁️ Visibility
* 🎚️ Atmospheric pressure
* 📅 Weather forecast

---

### 🤖 Conversational AI Weather Assistant

Users can communicate naturally with SkyCast instead of manually interpreting weather values.

The AI assistant can answer questions related to:

* Rain
* Outdoor activities
* Running
* Walking
* Clothing
* Umbrellas
* Sunscreen
* Sunglasses
* Hydration
* Wind
* Visibility
* Travel
* Weather safety

---

### 📍 My Location

SkyCast supports browser-based location detection.

```text
Browser Location
       ↓
Latitude + Longitude
       ↓
Reverse Geocoding
       ↓
City Detection
       ↓
Live Weather
```

---

### 💬 Context-Aware Conversations

SkyCast maintains recent conversation history so users can ask follow-up questions without repeatedly mentioning their location.

```text
User:
Is it going to rain today?

SkyCast:
There is a chance of rain today.

User:
Should I carry an umbrella?

SkyCast:
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
* ✨ Minimal modern dashboard

---

## 🏗️ System Architecture

```text
                         👤 USER
                           │
                           ▼
                ┌─────────────────────┐
                │   SkyCast Frontend  │
                │                     │
                │ HTML • CSS • JS     │
                └──────────┬──────────┘
                           │
                    REST API Requests
                           │
                           ▼
                ┌─────────────────────┐
                │    FastAPI Server   │
                │      Python         │
                └──────────┬──────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
     ┌─────────────────┐       ┌─────────────────┐
     │   wttr.in API   │       │  Weather Agent  │
     │ Live Weather    │       │    LangChain    │
     └────────┬────────┘       └────────┬────────┘
              │                         │
              │                         ▼
              │                ┌─────────────────┐
              │                │ Google Gemini   │
              │                │   2.5 Flash     │
              │                └────────┬────────┘
              │                         │
              └────────────┬────────────┘
                           ▼
                  🌦️ Weather Intelligence
                           │
                           ▼
                    💬 AI Response
```

---

## 🔄 How SkyCast Works

### 1. Select Location

The user searches for a city or uses **My Location**.

### 2. Retrieve Weather

The FastAPI backend requests current weather information from the weather service.

### 3. Prepare Context

The application combines:

```text
Live Weather Data
       +
Recent Conversation
       +
User Question
```

### 4. AI Processing

The weather context is passed to **Google Gemini** through the LangChain Google GenAI integration.

### 5. Generate Recommendation

Gemini interprets the weather conditions and generates a concise, practical response.

### 6. Display Result

The AI response is displayed in the SkyCast conversational interface.

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

### HTML5

Used to build the structure of the SkyCast dashboard, weather cards, navigation, quick prompts, and conversational interface.

### CSS3

Used for:

* Responsive layouts
* Dark/light themes
* Weather cards
* Animations
* Glassmorphism effects
* Chat bubbles
* Responsive mobile design

### JavaScript

Handles:

* Weather API requests
* AI chat requests
* Location detection
* Dynamic weather updates
* Chat history
* Quick prompts
* Theme switching
* Error handling

### Python

Used as the primary backend programming language.

### FastAPI

Provides the REST API layer between the frontend, weather service, and AI agent.

### LangChain

Used to integrate the Google Gemini model into the weather assistant workflow.

### Google Gemini

Provides the Generative AI capability that understands the user's weather-related questions and produces contextual recommendations.

### wttr.in

Provides live weather and forecast information used by the application.

---

## 🔌 API Endpoints

### `GET /`

Checks whether the SkyCast backend is running.

### `GET /weather`

Retrieves weather information for a city.

Example:

```text
/weather?city=Hyderabad
```

### `POST /ask`

Processes an AI weather question.

Example request:

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

---

## 🔐 Environment Configuration

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### Security

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

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd SkyCast
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

```env
GOOGLE_API_KEY=your_api_key
```

### 6. Start FastAPI

```bash
uvicorn backend.main:app --reload
```

### 7. Open the Frontend

Run the frontend using a local development server and open it in your browser.

---

## 📊 Example User Interaction

```text
🌡️ Hyderabad
29°C
Overcast
Feels like 31°C

Humidity: 63%
Wind: 17 km/h
Rain: 13%
UV: 0
Visibility: 10 km
Pressure: 1004 hPa
```

User:

```text
Is it too hot for a run?
```

SkyCast:

```text
At 29°C with a feels-like temperature of 31°C,
it's fairly warm for running. Stay hydrated and
consider running during a cooler part of the day.
```

---

## 🚀 Future Enhancements

* 🌧️ Advanced precipitation radar
* 🗺️ Interactive weather maps
* 🌬️ Air-quality monitoring
* 🔔 Severe weather alerts
* 📅 Extended forecasts
* 🎙️ Voice-based weather assistant
* 📊 Historical weather analytics
* 📱 Progressive Web App support
* ⚡ AI response caching
* 🌾 Weather-based agricultural recommendations
* 🤖 Specialized weather AI agents

---

## 🎯 Project Highlights

```text
🌦️ Real-Time Weather Data
        +
🤖 Generative AI
        +
🔗 LangChain
        +
🐍 FastAPI
        +
💻 Modern Web Interface
        =
☁️ SkyCast Weather Intelligence
```

---

## 👩‍💻 Developer

### Likhitha Sadi

**B.Tech — Information Technology**

**Areas of Interest**

* Artificial Intelligence
* Generative AI
* Full-Stack Development
* Python
* FastAPI
* Machine Learning
* Web Development

---

## ⭐ Project

If you find SkyCast useful or interesting, consider giving the repository a ⭐.

**Built with 🌦️ + 🤖 + 💻 using HTML, CSS, JavaScript, Python, FastAPI, LangChain and Google Gemini.**
