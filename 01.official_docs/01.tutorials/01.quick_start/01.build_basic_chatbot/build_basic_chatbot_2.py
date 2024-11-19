from dotenv import load_dotenv
load_dotenv()
from rich import print as rprint

from typing import Annotated

from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


llm = ChatOpenAI(model="gpt-4o-mini")


def chatbot(state: State):
    rprint(f'Node chatbot -> state: {state}')
    llm_response = llm.invoke(state["messages"])
    rprint(f'Node chatbot -> llm_response: {llm_response}')
    return {"messages": [llm_response]}


# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)
graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("chatbot")
graph = graph_builder.compile()


if "__main__" == __name__:
    mermaid_png = graph.get_graph().draw_mermaid_png()
    with open('diagram.png', 'wb') as f:
        f.write(mermaid_png)