from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


db = SqliteDb(db_file="tmp/data.db")

user_id = "jon_hamm@example.com"
session_id = "1001"

agent = Agent(
    model=Groq(id="qwen/qwen3-32b"),
    db=db,
    enable_session_summaries=True,
)

agent.print_response(
    "What can you tell me about quantum computing?",
    stream=True,
    user_id=user_id,
    session_id=session_id,
)

agent.print_response(
    "I would also like to know about LLMs?",
    stream=True,
    user_id=user_id,
    session_id=session_id
)

session_summary = agent.get_session_summary(session_id=session_id)
print(f"Session summary: {session_summary.summary}")