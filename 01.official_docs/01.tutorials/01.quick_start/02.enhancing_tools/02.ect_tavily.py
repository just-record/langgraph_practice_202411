from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults
from rich import print as rprint

tool = TavilySearchResults(max_results=2)
tools = [tool]
rprint(tool.invoke("What's a 'node' in LangGraph?"))
# [
#     {
#         'url': 'https://medium.com/@cplog/introduction-to-langgraph-a-beginners-guide-14f9be027141',
#         'content': 'Nodes: Nodes are the building blocks of your LangGraph. Each node represents a function or a computation step. You define nodes to perform specific tasks, such as processing input,making'
#     },
#     {
#         'url': 'https://www.datacamp.com/tutorial/langgraph-tutorial',
#         'content': "In LangGraph, each node represents an LLM agent, and the edges are the communication channels between these agents. This structure allows for clear and manageable workflows, where 
# each agent performs specific tasks and passes information to other agents as needed. State management. One of LangGraph's standout features is its automatic state"
#     }
# ]