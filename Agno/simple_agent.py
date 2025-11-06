from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = Groq(id="qwen/qwen3-32b")
tools = [DuckDuckGoTools()]

agent = Agent(
    model=model,
    description="you are an assistant that helps people find information on the internet",
    tools=tools,
    markdown=True,
)

agent.print_response("which team won the womens cricket world cup in 2025 and by how many runs or wickets?", stream=True)
