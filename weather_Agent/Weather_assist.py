from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import requests
import os

load_dotenv()

#print(os.getenv("GOOGLE_API_KEY"))  # Debug

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

user_query = input("Ask me anything: ")

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": user_query
        }
    ]
})

print(result["messages"][-1].content)