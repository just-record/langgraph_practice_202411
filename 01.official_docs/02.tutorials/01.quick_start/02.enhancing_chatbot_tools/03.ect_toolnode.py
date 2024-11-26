# A node that runs the tools called in the last AIMessage.
# <https://langchain-ai.github.io/langgraph/reference/prebuilt/?h=tools+condition#langgraph.prebuilt.tool_node.ToolNode>

### How to call tools using ToolNode
# <https://langchain-ai.github.io/langgraph/how-tos/tool-calling/?h=tool+node

from langchain_core.messages import AIMessage
from langchain_core.tools import tool

from langgraph.prebuilt import ToolNode

from rich import print as rprint

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


##################################################################################
### 1. 수동 호출
print('1.', '*'*50)
##################################################################################
message_with_single_tool_call = AIMessage(
    content="",
    tool_calls=[
        {
            "name": "get_weather",
            "args": {"location": "sf"},
            "id": "tool_call_id",
            "type": "tool_call",
        }
    ],
)

result = tool_node.invoke({"messages": [message_with_single_tool_call]})
rprint(result)
# 1. **************************************************
# {'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id')]}


##################################################################################
### 2. 수동 호출 - multiple
print('2.', '*'*50)
##################################################################################
message_with_multiple_tool_calls = AIMessage(
    content="",
    tool_calls=[
        {
            "name": "get_coolest_cities",
            "args": {},
            "id": "tool_call_id_1",
            "type": "tool_call",
        },
        {
            "name": "get_weather",
            "args": {"location": "sf"},
            "id": "tool_call_id_2",
            "type": "tool_call",
        },
    ],
)

result = tool_node.invoke({"messages": [message_with_multiple_tool_calls]})
rprint(result)
# {
#     'messages': [
#         ToolMessage(content='nyc, sf', name='get_coolest_cities', tool_call_id='tool_call_id_1'),
#         ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id_2')
#     ]
# }


##################################################################################
### 3. chat model와 함께 사용
# Tool messages가 반환됨
print('3.', '*'*50)
##################################################################################
from dotenv import load_dotenv
load_dotenv()


from typing import Literal

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState
from langgraph.prebuilt import ToolNode


model_with_tools = ChatOpenAI(
    model="gpt-4o-mini", temperature=0
).bind_tools(tools)


### model_with_tools invoke => tool call이 포함된 AIMessage 반환 ###
# rprint(model_with_tools.invoke("what's the weather in sf?"))
# AIMessage(
#     content='',
#     additional_kwargs={'tool_calls': [{'id': 'call_8C4wXS6q5QS2XkCU7jbbuSBD', 'function': {'arguments': '{"location":"San Francisco"}', 'name': 'get_weather'}, 'type': 'function'}], 'refusal': None}, 
#     response_metadata={
#         'token_usage': {
#             'completion_tokens': 15,
#             'prompt_tokens': 70,
#             'total_tokens': 85,
#             'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#             'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#         },
#         'model_name': 'gpt-4o-mini-2024-07-18',
#         'system_fingerprint': 'fp_0705bf87c0',
#         'finish_reason': 'tool_calls',
#         'logprobs': None
#     },
#     id='run-a1ce7576-1b3e-4d9c-a0af-b9ee44e844f0-0',
#     tool_calls=[{'name': 'get_weather', 'args': {'location': 'San Francisco'}, 'id': 'call_8C4wXS6q5QS2XkCU7jbbuSBD', 'type': 'tool_call'}],
#     usage_metadata={'input_tokens': 70, 'output_tokens': 15, 'total_tokens': 85, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# )

# rprint(model_with_tools.invoke("what's the weather in sf?").tool_calls)
# [{'name': 'get_weather', 'args': {'location': 'San Francisco'}, 'id': 'call_18ESI2SFmoRDIfbOTTXJ89uU', 'type': 'tool_call'}]

result = tool_node.invoke({"messages": [model_with_tools.invoke("what's the weather in sf?")]})
rprint(result)
# {'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='call_o8KuGXIPwcwbgpoxGrnQcoSe')]}


##################################################################################
### 4. ReAct Agent
print('4.', '*'*50)
##################################################################################
from typing import Literal

from langgraph.graph import StateGraph, MessagesState, START, END


def should_continue(state: MessagesState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END


def call_model(state: MessagesState):
    messages = state["messages"]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}


workflow = StateGraph(MessagesState)

# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue, ["tools", END])
workflow.add_edge("tools", "agent")

app = workflow.compile()


mermaid_png = app.get_graph().draw_mermaid_png()
with open('toolnode.png', 'wb') as f:
    f.write(mermaid_png)
    
    
### A. weather in sf?
# example with a single tool call
for chunk in app.stream(
    {"messages": [("human", "what's the weather in sf?")]}, stream_mode="values"
):
    chunk["messages"][-1].pretty_print()
# ================================ Human Message =================================

# what's the weather in sf?
# ================================== Ai Message ==================================
# Tool Calls:
#   get_weather (call_mkMFvPAGeEJpWynLdD5ou95L)
#  Call ID: call_mkMFvPAGeEJpWynLdD5ou95L
#   Args:
#     location: San Francisco
# ================================= Tool Message =================================
# Name: get_weather

# It's 60 degrees and foggy.
# ================================== Ai Message ==================================

# The weather in San Francisco is currently 60 degrees and foggy.    

print()
print()
print()
    
### B. the coolest cities?
# example with a multiple tool calls in succession

for chunk in app.stream(
    {"messages": [("human", "what's the weather in the coolest cities?")]},
    stream_mode="values",
):
    chunk["messages"][-1].pretty_print()
# ================================ Human Message =================================

# what's the weather in the coolest cities?
# ================================== Ai Message ==================================
# Tool Calls:
#   get_coolest_cities (call_SWVmU32a95PLxWf4oLF3mBbE)
#  Call ID: call_SWVmU32a95PLxWf4oLF3mBbE
#   Args:
# ================================= Tool Message =================================
# Name: get_coolest_cities

# nyc, sf
# ================================== Ai Message ==================================
# Tool Calls:
#   get_weather (call_wPbF7QtEPMCfmJBPef6p9cAx)
#  Call ID: call_wPbF7QtEPMCfmJBPef6p9cAx
#   Args:
#     location: nyc
#   get_weather (call_fUinvJHBS0X4176FFfMu5CpM)
#  Call ID: call_fUinvJHBS0X4176FFfMu5CpM
#   Args:
#     location: sf
# ================================= Tool Message =================================
# Name: get_weather

# It's 60 degrees and foggy.
# ================================== Ai Message ==================================

# The current weather in the coolest cities is as follows:

# - **New York City (NYC)**: 90 degrees and sunny.
# - **San Francisco (SF)**: 60 degrees and foggy.    