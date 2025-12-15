from agno.agent import Agent
from agno.team import Team
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = Groq(id="llama-3.3-70b-versatile")
# tools = [DuckDuckGoTools(), YFinanceTools()]

web_agent = Agent(
    name="WebAgent",
    model=model,
    description="you are an assistant that helps people find information on the internet",
    instructions="Always include the sources you used to find the information in your final answer.",
    tools=[DuckDuckGoTools()],
    # show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="FinanceAgent",
    model=model,
    instructions="Use tables to display data",
    # tools=[YFinanceTools(stock_prices=True, company_info=True, analyst_recommendations=True,  stock_fundamentals=True)],
    tools=[YFinanceTools()],
    # show_tool_calls=True,
    markdown=True,
)

agent_team = Team(
    name="InfoFinanceTeam",
    members=[web_agent, finance_agent],
    model=model,
    instructions=['Always include the sources you used to find the information in your final answer.', 'Use tables to display data'],
    # show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Analyze companies like tesla, NVDA, Apple and suggest which stock to buy for long term investment based on their recent performance and news about them.")
