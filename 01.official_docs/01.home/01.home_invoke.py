from dotenv import load_dotenv
load_dotenv()

import home
from langchain_core.messages import HumanMessage

from rich import print as rprint

##################################################################################
### 1. graph를 invoke 하기 - sf 날씨 물어보기 - tool call 호출
print('1', '*'*50)
##################################################################################
final_state = home.app.invoke(
    {"messages": [HumanMessage(content="what is the weather in sf")]},
    config={"configurable": {"thread_id": 42}}
)
print(final_state["messages"][-1].content)
# 1 **************************************************
# === call_model(NODE) -> state['messages'][-1].content ===: what is the weather in sf
# === should_continue(NODE?) -> state['messages'][-1].tool_calls ===: [{'name': 'search', 'args': {'query': 'current weather in San Francisco'}, 'id': 'call_UrWDkajyYvNeMxpiZH2drfT3', 'type': 'tool_call'}]
# === search(TOOL) -> query ===: current weather in San Francisco
# === call_model(NODE) -> state['messages'][-1].content ===: It's 60 degrees and foggy.
# === should_continue(NODE?) -> state['messages'][-1].tool_calls ===: []
# The current weather in San Francisco is 60 degrees and foggy.


##################################################################################
### 2. ny 날씨 물어보기 - tool call 호출
print('2', '*'*50)
##################################################################################
final_state = home.app.invoke(
    {"messages": [HumanMessage(content="what about ny")]},
    config={"configurable": {"thread_id": 42}}
)
print(final_state["messages"][-1].content)
# 2 **************************************************
# === call_model(NODE) -> state['messages'][-1].content ===: what about ny
# === should_continue(NODE?) -> state['messages'][-1].tool_calls ===: [{'name': 'search', 'args': {'query': 'current weather in New York'}, 'id': 'call_9l6vudhj6bZAGgmnokN4EFz4', 'type': 'tool_call'}]
# === search(TOOL) -> query ===: current weather in New York
# === call_model(NODE) -> state['messages'][-1].content ===: It's 90 degrees and sunny.
# === should_continue(NODE?) -> state['messages'][-1].tool_calls ===: []
# The current weather in New York is 90 degrees and sunny.


##################################################################################
### 3. tool과 관계 없는 질문 - tool call 없음
print('3', '*'*50)
##################################################################################
final_state = home.app.invoke(
    {"messages": [HumanMessage(content="who are you?")]},
    config={"configurable": {"thread_id": 42}}
)
print(final_state["messages"][-1].content)
# 3 **************************************************
# === call_model(NODE) -> state['messages'][-1].content ===: who are you?
# === should_continue(NODE?) -> state['messages'][-1].tool_calls ===: []
# I am an AI language model designed to assist with a variety of tasks, including answering questions, providing information, and helping with problem-solving. How can I assist you today?