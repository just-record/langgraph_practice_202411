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
# tool = TavilySearchResults(max_results=2)
# tools = [tool]
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
    interrupt_before=["tools"],
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
    
### 멈춘 상태에서 1-1.코드 - None으로 진행 시키지 않고 2.번 코드로 새로운 요청을 진행하면 오류 발생 ###
# ================================ Human Message =================================
# what's the weather in the coolest cities?
# ...
# openai.BadRequestError: Error code: 400 - {'error': {'message': "An assistant message with 'tool_calls' must be followed by tool messages responding to each 'tool_call_id'. The following tool_call_ids did not have response messages: call_3Gi3p7hzFhK5NG1TGq8Exp96", 'type': 'invalid_request_error', 'param': 'messages.[2].role', 'code': None}}

#####################################
### 1-1. None으로 graph 진행 시키기 ###
#####################################
print('1-1.', '+'*30)
events = graph.stream(None, config, stream_mode="values")
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()    
    
    
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

#####################################
### 2-1. None으로 graph 진행 시키기 ###
#####################################
print('2-1.', '+'*30)
events = graph.stream(None, config, stream_mode="values")
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
        
        
##################################################################################
### [[ tools 에 여러 개의 tool을 설정해도 잘 작동 함 ]] ###

##################################################################################
### [[ 음~~~ 특정 tool만 interrupt를 걸고 싶다면??? ]] ###