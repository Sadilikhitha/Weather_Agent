# 🌦️ LangChain Weather Agent

A simple AI-powered Weather Agent built using **LangChain**, **Google Gemini**, and a custom weather tool. The agent understands natural language queries, determines when to use the weather tool, and returns the current weather for a specified city.

---

## 🚀 Features

* 🤖 AI agent powered by Google Gemini 2.5 Flash
* 🛠️ Custom LangChain Tool for weather retrieval
* 🌍 Fetches real-time weather information using `wttr.in`
* 💬 Accepts natural language queries
* 🔐 Secure API key management using `.env`

---

## 📁 Project Structure

```
Weather_Agent/
│── main.py
│── .env
│── .gitignore
│── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* LangChain
* Google Gemini 2.5 Flash
* LangChain Google GenAI
* Requests
* Python Dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Weather_Agent.git
```

### 2. Navigate to the project folder

```bash
cd Weather_Agent
```

### 3. Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate it

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
```

> **Important:** Never upload your `.env` file to GitHub. Add `.env` to your `.gitignore` file.

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💡 Example

**Input**

```
Ask me anything:
What's the weather in Hyderabad?
```

**Output**

```
The weather in Hyderabad is Partly cloudy +30°C
```

---

## ⚙️ How It Works

1. Loads the Google Gemini API key from the `.env` file.
2. Initializes the Gemini 2.5 Flash language model.
3. Defines a custom LangChain tool (`get_weather`) that fetches weather data from `wttr.in`.
4. Creates a LangChain agent with the weather tool.
5. Accepts a user's natural language query.
6. The AI agent decides whether to invoke the weather tool.
7. Returns the weather information in a human-friendly format.

---

## 📄 Requirements

```
langchain
langchain-google-genai
python-dotenv
requests
```

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔒 Security

This project uses a `.env` file to securely store API keys.

Ensure your `.gitignore` contains:

```
.env
```

This prevents sensitive credentials from being pushed to GitHub.

---

## 📜 License

This project is open source and available under the MIT License.

---

## 👩‍💻 Author

**Likhitha Sadi**

Built as a beginner-friendly project to explore AI Agents, LangChain, and Google Gemini.
