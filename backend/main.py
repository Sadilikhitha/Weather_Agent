from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.weather_agent import (
    ask_weather_agent,
    get_weather_data
)


app = FastAPI(
    title="SkyCast Weather AI"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message":
        "SkyCast Weather AI API is running"
    }


@app.get("/weather")
def weather(city: str):

    try:

        return get_weather_data(city)

    except Exception as e:

        print(
            "WEATHER ERROR:",
            repr(e)
        )

        return {
            "detail": str(e)
        }


@app.post("/ask")
def ask_weather(request: dict):

    question = request.get(
        "question",
        ""
    ).strip()


    weather_data = request.get(
        "weather_data"
    )


    chat_history = request.get(
        "chat_history",
        []
    )


    if not question:

        return {
            "detail":
            "Question is required"
        }


    try:

        answer = ask_weather_agent(
            user_query=question,
            weather_data=weather_data,
            chat_history=chat_history
        )


        return {
            "answer": answer
        }


    except Exception as e:

        print(
            "ASK ERROR:",
            repr(e)
        )

        return {
            "detail": str(e)
        }