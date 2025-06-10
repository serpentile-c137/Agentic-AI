from pydantic import BaseModel, Field
from agents import Agent
from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os

load_dotenv(override=True)
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME='llama-3.1-8b-instant'

groq_client = AsyncOpenAI(base_url=BASE_URL, api_key=os.getenv("GROQ_API_KEY"))
custom_model = OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=groq_client)

HOW_MANY_SEARCHES = 5

INSTRUCTIONS = f"You are a helpful research assistant. Given a query, come up with a set of web searches \
to perform to best answer the query. Output {HOW_MANY_SEARCHES} terms to query for."


class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")
    
planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model=custom_model,
    output_type=WebSearchPlan,
)