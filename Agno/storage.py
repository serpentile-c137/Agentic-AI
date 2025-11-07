from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
     model=Groq(id="qwen/qwen3-32b"),
    # Fix the session id to continue the same session across execution cycles
    session_id="fixed_id_for_demo",
    db=SqliteDb(db_file="tmp/data.db"),
    # Make the agent aware of the session history
    add_history_to_context=True,
    num_history_runs=3,
)
agent.print_response("Hi! my name is Darth Vader.")
agent.print_response("What was my last question?")
agent.print_response("What is my name?")
agent.print_response("What was my last question?")
pprint(agent.get_messages_for_session())