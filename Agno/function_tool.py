from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = Groq(id="qwen/qwen3-32b")

def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers and returns the result."""
    return a * b

def add_numbers(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    """Subtracts the second number from the first and returns the result."""
    return a - b

agent = Agent(
    model=model,
    description="you are a math assistant that helps people perform basic arithmetic operations",
    tools=[multiply_numbers, add_numbers, subtract_numbers],
    instructions="show tool calls and calculations",
    markdown=True,
)

agent.print_response("What is the result of adding 15 and 27, then multiplying the sum by 3, and finally subtracting 10?", stream=True)