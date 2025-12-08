from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

model = OpenAIChat(id="gpt-40-mini")
tools = [DuckDuckGoTools()]

agent = Agent(
    model=model,
    description="you are an assistant that helps people find information on the internet",
    tools=tools,
    markdown=True,
)

agent.print_response("which team won the womens cricket world cup in 2025 and by how many runs or wickets?", stream=True)
