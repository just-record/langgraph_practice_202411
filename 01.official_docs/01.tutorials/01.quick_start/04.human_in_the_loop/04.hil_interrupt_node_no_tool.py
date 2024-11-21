### node에 interrupt가 걸리는 것 같다. ###
### 특정 tool를 실행 시킬 때 interrupt를 걸고 싶다면 node를 따로 만들고 그 node에 tool을 연결? ###
### 우선 node에 tool을 연결하지 않고 테스 해보자. ###
### 도시의 날씨와 가장 추운 도시를 각각 node로 생성 ###

### [[ 많이 엉성하게 설계하고 코딩 했지만 그래도 동작은 한다. ]] ###
### get_coolest_cities node는 그냥 실행 되고 get_weather node는 실행 전에 interrupt 된다. ###


###################################################
### 그런데 가만히 생각 해 보니 node에 tool을 연결??? ###
### 어차피 nodr가 함순데 무슨 tool을 연결???        ###
### 분석을 계속 하다 보면 뭐가 나오겠지...           ###
###################################################

from typing import Annotated

from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
# from langgraph.prebuilt import ToolNode, tools_condition
# from langchain_core.tools import tool


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

### Tool 정의 ###
# @tool
# def get_weather(location: str):
#     """Call to get the current weather."""
#     if location.lower() in ["sf", "san francisco"]:
#         return "It's 60 degrees and foggy."
#     else:
#         return "It's 90 degrees and sunny."


# @tool
# def get_coolest_cities():
#     """Get a list of coolest cities"""
#     return "nyc, sf"


# tools = [get_weather, get_coolest_cities]
# tool_node = ToolNode(tools=tools)
llm = ChatOpenAI(model="gpt-4o-mini")
# llm_with_tools = llm.bind_tools(tools)


def chatbot(state: State):
    # return {"messages": [llm_with_tools.invoke(state["messages"])]}
    prompt = "[사용자 질문]을 보고 가장 추운 도시를 물으면 get_coolest_cities tool을 반환하고 나머지는 get_weather을 반환해줘.\n\n[사용자 질문]: "
    query = state["messages"][-1].content
    humanMessage = state["messages"][-1]
    humanMessage.content = prompt + query
    return {"messages": llm.invoke([humanMessage])}


### 도시의 날씨, 가장 추운 도시 node 생성 ###
def get_weather(state: State):
    print('node: get_weather')
    print(f'state: {state}')
    return {"messages": [{"role": "assistant", "content": "It's 60 degrees and foggy.", "name": "get_weather", "tool_call_id": "tool_call_id"}]}


def get_coolest_cities(state: State):
    print('node: get_coolest_cities')
    print(f'state: {state}')
    return {"messages": [{"role": "assistant", "content": "nyc, sf", "name": "get_coolest_cities", "tool_call_id": "tool_call_id"}]}


def check_response(state: State):
    response = state["messages"][-1].content
    if "get_coolest_cities" in response:
        return "get_coolest_cities"
    return "get_weather"


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("get_weather", get_weather)
graph_builder.add_node("get_coolest_cities", get_coolest_cities)

graph_builder.add_conditional_edges(
    "chatbot",
    check_response,
)
# graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("get_weather")
graph_builder.set_finish_point("get_coolest_cities")

memory = MemorySaver()
graph = graph_builder.compile(
    checkpointer=memory,
    # interrupt_before=["tools"],
    interrupt_before=["get_weather"],   # get_weather node에서 interrupt
)

mermaid_png = graph.get_graph().draw_mermaid_png()
with open('interrupt_node.png', 'wb') as f:
    f.write(mermaid_png)
    

config = {"configurable": {"thread_id": "1"}}
##################################################################################
### 1. 가장 추운 도시
print('1.', '*'*50)
##################################################################################
for chunk in graph.stream(
    {"messages": [("human", "what's the weather in the coolest cities?")]},
    config,
    stream_mode="values",
):
    chunk["messages"][-1].pretty_print()   
    
    
##################################################################################
### 2. 도시의 날씨 정보
print('2.', '*'*50)
##################################################################################
for chunk in graph.stream(
    {"messages": [("human", "what's the weather in sf?")]},
    config,
    stream_mode="values",
    
):
    chunk["messages"][-1].pretty_print()    
    

events = graph.stream(None, config, stream_mode="values")
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()  

