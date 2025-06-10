import os
from typing import Dict
from agents import Agent, function_tool
import asyncio
import requests
from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI

load_dotenv(override=True)
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME='llama-3.1-8b-instant'

groq_client = AsyncOpenAI(base_url=BASE_URL, api_key=os.getenv("GROQ_API_KEY"))
custom_model = OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=groq_client)

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send out an email with the given subject and HTML body to all sales prospects using Resend"""
    
    # Replace with your actual verified sender and target recipient
    from_email = "ed@edwarddonner.com"
    to_email = "shardulggore@gmail.com"
    
    # Get the Resend API key from environment variable
    RESEND_API_KEY = os.environ.get("RESEND_API_KEY")
    
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from": f"Ed Donner <{from_email}>",
        "to": [to_email],
        "subject": subject,
        "html": html_body
    }
    
    response = requests.post("https://api.resend.com/emails", json=payload, headers=headers)
    
    if response.status_code == 202:
        return {"status": "success"}
    else:
        return {"status": "failure", "message": response.text}

INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model=custom_model,
)
