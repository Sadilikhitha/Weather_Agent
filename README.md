# 🌦️ SkyCast Weather AI

> An AI-powered weather assistant that combines live weather data with Google Gemini to provide conversational weather information and practical recommendations.

<p align="center">
  <img src="screenshots/skycast-dashboard.png" alt="SkyCast Weather AI Dashboard" width="900">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white">
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white">
</p>

---

## 🚀 Live Demo

* **Live Application:** weatheragent-frontend-chi.vercel.app
* **Backend API:** [SkyCast Weather AI API](https://weather-agent-app-fra0.onrender.com/?utm_source=chatgpt.com)

---

## 📌 Overview

**SkyCast Weather AI** is a conversational weather assistant that uses live weather information and Google Gemini to answer weather-related questions.

The application allows users to:

* Search for weather by location
* View current weather conditions
* Check upcoming weather forecasts
* Ask questions in natural language
* Get practical weather-based recommendations
* Ask follow-up questions without repeatedly providing the location
* Use browser location to get weather for their current location

Instead of relying only on an AI model, SkyCast provides live weather information as context to Gemini before generating a response.

---

## ✨ Features

### 🌤️ Weather Information

* Current temperature
* Feels-like temperature
* Weather condition
* Humidity
* Wind speed
* Wind direction
* Atmospheric pressure
* Visibility
* UV index
* Precipitation
* Five-day forecast
* Daily maximum and minimum temperatures
* Rain probability

### 🤖 AI Weather Assistant

Users can ask natural-language questions such as:

```text
Will it rain today?

What should I wear?

Should I carry an umbrella?

Is it good for outdoor activities?

Is it too hot for a run?
```

The AI uses the available weather information to provide a contextual response.

### 🧳 Trip Recommendations

SkyCast can provide practical recommendations based on weather conditions, including:

* 👕 Clothing
* ☂️ Umbrella
* 🧴 Sunscreen
* 🕶️ Sunglasses
* 💧 Hydration
* 👟 Footwear
* 🌤️ Outdoor activities
* 🚗 Travel considerations

### 📍 Location Support

SkyCast supports both:

* Manual location search
* Browser-based geolocation

When the user gives location permission, the application can use their current browser location rather than being restricted to one city.

### 💬 Conversational Context

SkyCast supports follow-up questions.

Example:

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
Light and breathable clothing would be comfortable.
```

The latest conversation messages are used to maintain context.

---

## 🏗️ How It Works

```text
                User
                  │
                  ▼
        ┌─────────────────┐
        │ SkyCast Frontend│
        │ HTML/CSS/JS     │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ FastAPI Backend │
        └────────┬────────┘
                 │
          ┌──────┴──────┐
          ▼             ▼
   Weather Service   Google Gemini
          │             │
          └──────┬──────┘
                 ▼
        AI Weather Response
                 │
                 ▼
                User
```

The frontend sends the user's question, weather information, and recent conversation history to the FastAPI backend.

The backend passes this information to the weather agent, which uses Google Gemini to generate the final response.

---

## 🛠️ Tech Stack

| Technology        | Purpose                    |
| ----------------- | -------------------------- |
| **HTML5**         | Frontend structure         |
| **CSS3**          | User interface and styling |
| **JavaScript**    | Frontend functionality     |
| **Python**        | Backend development        |
| **FastAPI**       | REST API                   |
| **Google Gemini** | Generative AI              |
| **LangChain**     | Gemini integration         |
| **wttr.in**       | Weather data               |
| **Requests**      | HTTP requests              |
| **python-dotenv** | Environment variables      |
| **Vercel**        | Frontend deployment        |
| **Render**        | Backend deployment         |

---

## 📂 Project Structure

```text
Weather_Agent-main/
│
├── backend/
│   ├── main.py
│   └── weather_agent.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── package-lock.json
│
├── Weather_Agent/
│
├── .gitignore
├── .gitattributes
├── requirements.txt
├── info.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sadilikhitha/Weather_Agent.git
```

```bash
cd Weather_Agent
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

For Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Keep your API key private and **never upload `.env` to GitHub**.

---

## ▶️ Run the Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🌐 Run the Frontend

The frontend is built using plain HTML, CSS, and JavaScript.

Open another terminal:

```bash
cd frontend
```

Run:

```bash
python -m http.server 5500
```

Then open:

```text
http://localhost:5500
```

---

## 🔗 API Endpoints

### Weather

```http
GET /weather?city={city}
```

Example:

```text
/weather?city=Hyderabad
```

Returns current weather and forecast information.

### AI Assistant

```http
POST /ask
```

The endpoint accepts the user's question along with weather data and conversation history and returns an AI-generated response.

---

## 🚀 Deployment

### Backend

The FastAPI backend is deployed on **Render**.

[SkyCast Weather AI Backend](https://weather-agent-app-fra0.onrender.com/?utm_source=chatgpt.com)

### Frontend

The frontend is deployed separately on **Vercel**.

The frontend communicates with the Render backend using the deployed API URL.

```javascript
const API = "https://weather-agent-app-fra0.onrender.com";
```

---

## 📸 Screenshots

Create a folder named:

```text
screenshots/
```

Inside it, add screenshots of your application:

```text
screenshots/
├── skycast-dashboard.png
├── skycast-weather.png
├── skycast-chat.png
└── skycast-location.png
```

Then add them to the README like this:

### Dashboard

<p align="center">
  <img src="screenshots/skycast-dashboard.png" alt="SkyCast Dashboard" width="900">
</p>

### Weather Information

<p align="center">
  <img src="screenshots/skycast-weather.png" alt="SkyCast Weather" width="900">
</p>

### AI Chat

<p align="center">
  <img src="screenshots/skycast-chat.png" alt="SkyCast AI Chat" width="900">
</p>

### Location-Based Weather

<p align="center">
  <img src="screenshots/skycast-location.png" alt="SkyCast Location Weather" width="900">
</p>

---

## 💡 Example Questions

```text
Will it rain today?

What should I wear today?

Should I carry an umbrella?

Is it suitable for outdoor activities?

What is the weather tomorrow?

Is it too hot for a run?

What should I carry for my trip?

Which day is suitable for sightseeing?
```

---

## 🔮 Future Improvements

* Hourly weather forecasts
* Weather alerts and notifications
* Interactive weather maps
* Improved trip planning
* More detailed activity recommendations
* Weather history and trends
* Additional weather data sources
* User authentication
* Persistent conversation history
* Mobile application

---

## 👩‍💻 Author

### Likhitha Sadi

GitHub: [Weather_Agent Repository](https://github.com/Sadilikhitha/Weather_Agent?utm_source=chatgpt.com)

---

## ⭐ Project

**SkyCast Weather AI** combines:

```text
🌦️ Live Weather Data
        +
🤖 Google Gemini
        +
🔗 LangChain
        +
🐍 Python / FastAPI
        +
💻 JavaScript
        ↓
Conversational Weather Intelligence
```

> Built as a practical Generative AI application for weather assistance and travel recommendations.
