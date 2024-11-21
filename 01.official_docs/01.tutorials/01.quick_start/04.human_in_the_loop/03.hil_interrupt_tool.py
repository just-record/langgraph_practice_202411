### 특정 tool만 interrupt를 걸어 보고 싶었다. ###
### interrupt_before=[get_coolest_cities]와 같이 특정 tool만 설정했다. ###
### 원래는 interrupt_before=["tools"]로 tools_node를 interrupt 했었다. ###

### [[ 오류 발생 ]] ###
### 특정 tool은 interrupt 되지 않는다. ###
### 아마 node를 interrupt 하나 보다. ###

#################################################
# if node not in self.nodes:
# TypeError: unhashable type: 'StructuredTool'
################################################# 

### [[ 특정 tool를 실행 시킬 때 interrupt를 걸고 싶다면 node를 따로 만들고 그 node에 tool을 연결? ]] ###

from typing import Annotated

from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

### Tool 정의 ###
@tool
def get_weather(location: str):
    """Call to get the current weather."""
    if location.lower() in ["sf", "san francisco"]:
        return "It's 60 degrees and foggy."
    else:
        return "It's 90 degrees and sunny."


@tool
def get_coolest_cities():
    """Get a list of coolest cities"""
    return "nyc, sf"


tools = [get_weather, get_coolest_cities]
tool_node = ToolNode(tools=tools)
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools)


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")

memory = MemorySaver()
graph = graph_builder.compile(
    checkpointer=memory,
    # interrupt_before=["tools"],
    ######################################
    ### tools node가 아닌 tool에 interrupt 걸기 ###
    interrupt_before=[get_coolest_cities],
)

mermaid_png = graph.get_graph().draw_mermaid_png()
with open('toolnode.png', 'wb') as f:
    f.write(mermaid_png)
    

config = {"configurable": {"thread_id": "1"}}
##################################################################################
### 1. 도시의 날씨 정보
print('1.', '*'*50)
##################################################################################
for chunk in graph.stream(
    {"messages": [("human", "what's the weather in sf?")]},
    config,
    stream_mode="values",
    
):
    chunk["messages"][-1].pretty_print()    
    
    
##################################################################################
### 2. 가장 추운 도시
print('2.', '*'*50)
##################################################################################
for chunk in graph.stream(
    {"messages": [("human", "what's the weather in the coolest cities?")]},
    config,
    stream_mode="values",
):
    chunk["messages"][-1].pretty_print()   
