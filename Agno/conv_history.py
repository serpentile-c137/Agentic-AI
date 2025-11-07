# Agno/conv_history.py
from agno.agent import Agent  # [web:15]
from agno.models.groq import Groq  # [web:20]
from agno.os import AgentOS  # [web:15]
from local_storage import load_social_media_storage  # returns SqliteDb [web:51]

db = load_social_media_storage()  # SqliteDb [web:51]

agent = Agent(
    name="SocialMediaAgent",
    model=Groq(id="llama-3.3-70b-versatile"),  # Groq model id [web:20]
    description="you are an assistant that helps people manage their social media accounts",  # [web:15]
    instructions="Be concise and clear in your responses.",  # [web:15]
    db=db,  # attach SQLite DB for memory [web:51]
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,  # render markdown [web:15]
)

agent_os = AgentOS(agents=[agent])  # [web:15]
app = agent_os.get_app()  # [web:15]

if __name__ == "__main__":
    agent_os.serve(app="Agno.conv_history:app", reload=True)  # adjust module:app path as needed [web:15]
