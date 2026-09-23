from fastapi import FastAPI
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import requests
import os

app = FastAPI()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

@tool
def get_weather(city: str):
    """Fetches weather data"""
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"


agent = create_agent(
    model=llm,
    tools=[get_weather]
)


class WeatherRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "Weather Agent is running"}


@app.post("/weather")
def weather(request: WeatherRequest):

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": request.query
            }
        ]
    })

    return {
        "response": result["messages"][-1].content
    }
