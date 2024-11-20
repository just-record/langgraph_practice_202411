### add_messages 대신 다른 함수 사용 가능한가? ###

from rich import print as rprint
# from langgraph.graph.message import add_messages

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph


def print_messages(msgs1, msgs2):
    print('msgs1:', msgs1, 'mssg2:', msgs2)
    ######################
    ### 1. reutrn None ###
    ######################
    # return None
    
    ######################
    ### 2. reutrn msg2 ###
    ######################
    return msgs2


class State(TypedDict):
    # messages: Annotated[list, add_messages]
    messages: Annotated[list, print_messages]


def chatbot(state: State):
    rprint(f'Node chatbot -> state: {state}')
    return {"messages": [("assistant", "Hello")]}


builder = StateGraph(State)
# builder.add_node("chatbot", lambda state: {"messages": [("assistant", "Hello")]})
builder.add_node("chatbot", chatbot)
builder.set_entry_point("chatbot")
builder.set_finish_point("chatbot")
graph = builder.compile()
rprint(graph.invoke({"messages": [("user", "hi")]}))

### 1. return None ###
# msgs1: [] mssg2: [('user', 'hi')]
# Node chatbot -> state: {'messages': None}
# msgs1: None mssg2: [('assistant', 'Hello')]
# {'messages': None}


### 2. return msg2 ###
# msgs1: [] mssg2: [('user', 'hi')]
# Node chatbot -> state: {'messages': [('user', 'hi')]}
# msgs1: [('user', 'hi')] mssg2: [('assistant', 'Hello')]
# {'messages': [('assistant', 'Hello')]}

##################################################################################
### 1. return None 
### 초기화: chatbot 호출 - 입력값에 {messages: [("user", "hi")]}
### chatbot의 arguments의 state는 입력 값이 아닌 이전의 state를 받는 것 같다. -> None
### chatbot가 실행: messages가 있으면 State의 print_messages가 호출
### print_messages의 return값은 None이고 State의 messages는 None이 저장된다.
### chatbot의 return값은 {"messages": [("assistant", "Hello")]}이다. => 어디에 쓰일까?
### END 노드: 입력 값은 위의 chatbot의 return 값인듯?  {"messages": [("assistant", "Hello")]}
### print_messages는 {"messages": None}를 저장하고 있어 1개의 messages가 출력된다.
### END(invoke)의 return값은 {"messages": None}이다. => state return값을 return값으로 사용하는 것 같다.
##################################################################################

##################################################################################
### 1. return msgs2
### 초기화: chatbot 호출 - 입력값에 {messages: [("user", "hi")]}
### chatbot의 arguments의 state는 입력 값이 아닌 이전의 state를 받는 것 같다. -> None
### chatbot가 실행: messages가 있으면 State의 print_messages가 호출
### print_messages의 return값은 {"messages": [("user", "hi")]}이고 State의 messages는 이 값이 저장된다.
### chatbot의 return값은 {"messages": [("assistant", "Hello")]}이다. => 어디에 쓰일까?
### END 노드: 입력 값은 위의 chatbot의 return 값인듯?  {"messages": [("assistant", "Hello")]}
### print_messages는 {"messages": [("user", "hi")]}를 저장하고 있어 2개의 messages가 출력된다.
### END(invoke)의 return값은 {"messages": [("assistant", "Hello")]}이다. => state return값을 return값으로 사용하는 것 같다.
##################################################################################