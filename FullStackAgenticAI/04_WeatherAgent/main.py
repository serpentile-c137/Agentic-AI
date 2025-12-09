from openai import OpenAI
from dotenv import load_dotenv
import requests
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        print("Weather API Response:")
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"


def main():
    user_query = input("> ")
    
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            { "role": "user", "content": user_query }
        ]
    )

    print(f"🤖: {response.choices[0].message.content}")

# print(get_weather("airoli"))
main()