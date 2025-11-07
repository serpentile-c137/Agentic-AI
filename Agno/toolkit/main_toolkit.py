from agno.agent import Agent
from agno.models.groq import Groq
# from agno.tools.math_toolkit import MathToolkit
from math_toolkit import MathToolkit
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = Groq(id="qwen/qwen3-32b")

agent = Agent(
    model=model,
    description="you are an assistant that helps people with mathematical calculations",
    instructions="Use the math toolkit to perform calculations as needed and give result in markdown.",
    tools=[MathToolkit()],
    markdown=True,
)

agent.print_response("what is fifteen divided by three", stream=True)