from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

search_tool = TavilySearchResults(search_depth='basic')

tools = [search_tool]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

agent.invoke("Give me a funny tweet about todays weather in mumbai")

# result = llm.invoke("Write a poem about a lonely computer")

# print(result)