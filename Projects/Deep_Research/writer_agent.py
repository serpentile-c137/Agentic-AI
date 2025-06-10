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

INSTRUCTIONS = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 5-10 pages of content, at least 1000 words."
)


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")

    markdown_report: str = Field(description="The final report")

    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS,
    model=custom_model,
    output_type=ReportData,
)