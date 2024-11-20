from rich import print as rprint
# from langgraph.graph.message import add_messages

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph


def print_messages(msgs1, msgs2):
    print('msgs1:', msgs1, 'mssg2:', msgs2)
    return msgs2


def update_time(time1, time2):
    print('time1:', time1, 'time2:', time2)
    return time2


class State(TypedDict):
    # messages: Annotated[list, add_messages]
    messages: Annotated[list, print_messages]
    last_updated: Annotated[str , update_time]
    


def chatbot(state: State):
    rprint(f'Node chatbot -> state: {state}')
    return {"messages": [("assistant", "Hello")], "last_updated": "2024년 11월 20일"}
    # return "chatbot return"


builder = StateGraph(State)
# builder.add_node("chatbot", lambda state: {"messages": [("assistant", "Hello")]})
builder.add_node("chatbot", chatbot)
builder.set_entry_point("chatbot")
builder.set_finish_point("chatbot")
graph = builder.compile()
# rprint(graph.invoke({"messages": [("user", "hi")]}))

##################################################################################
### 1. invoke시에 입력 값 없이
print('1.', '*'*50)
##################################################################################
# rprint(graph.invoke())
### [[오류 발생]] ###
# TypeError: Pregel.invoke() missing 1 required positional argument: 'input'

##################################################################################
### 2. invoke시에 input={}로 입력
print('2.', '*'*50)
##################################################################################
# rprint(graph.invoke(input={}))
### [[오류 발생]] ###
# langgraph.errors.InvalidUpdateError: Expected node messages to update at least one of ['messages', 'last_updated'], got {}

##################################################################################
### 3. invoke시에 messages만 input={'messages': [("user", "hi")]}로 입력
print('3.', '*'*50)
##################################################################################
rprint(graph.invoke({'messages': [("user", "hi")]}))
# 3. **************************************************
# msgs1: [] mssg2: [('user', 'hi')]
# Node chatbot -> state: {'messages': [('user', 'hi')], 'last_updated': ''}
# msgs1: [('user', 'hi')] mssg2: [('assistant', 'Hello')]
# time1:  time2: 2024년 11월 20일
# {'messages': [('assistant', 'Hello')], 'last_updated': '2024년 11월 20일'}


##################################################################################
### 4. invoke시에 last_updated만 input={'last_updated': "2024년 11월 19일"}로 입력
print('4.', '*'*50)
##################################################################################
rprint(graph.invoke({'last_updated': "2024년 11월 19일"}))
# 4. **************************************************
# time1:  time2: 2024년 11월 19일
# Node chatbot -> state: {'messages': [], 'last_updated': '2024년 11월 19일'}
# msgs1: [] mssg2: [('assistant', 'Hello')]
# time1: 2024년 11월 19일 time2: 2024년 11월 20일
# {'messages': [('assistant', 'Hello')], 'last_updated': '2024년 11월 20일'}


##################################################################################
### 5. invoke시에 messages와 last_updated 둘다 입력
print('5.', '*'*50)
##################################################################################
rprint(graph.invoke({'messages': [("user", "hi")], 'last_updated': "2024년 11월 19일"}))
# msgs1: [] mssg2: [('user', 'hi')]
# time1:  time2: 2024년 11월 19일
# Node chatbot -> state: {'messages': [('user', 'hi')], 'last_updated': '2024년 11월 19일'}
# msgs1: [('user', 'hi')] mssg2: [('assistant', 'Hello')]
# time1: 2024년 11월 19일 time2: 2024년 11월 20일
# {'messages': [('assistant', 'Hello')], 'last_updated': '2024년 11월 20일'}