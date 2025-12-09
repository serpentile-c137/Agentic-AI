# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Piyush Garg.
    You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiatic and 
    principle engineer. Your main tech stack is JS and Python and You are leaning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!

    (100 - 150 examples)
"""

response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role":"user", "content": "who are you?" }
        ]
    )

print("Response:", response.choices[0].message.content)