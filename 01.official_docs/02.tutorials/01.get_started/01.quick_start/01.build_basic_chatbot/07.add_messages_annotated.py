# class State(TypedDict):
#     messages: Annotated[list, add_messages]

### [[messages는 Annotated에 의해 list타입이며 add_messages로 주석이 달림]] ###
### add_messages는 함수며 언제 어떤 값으로 호출 되는가? ###

# 공식 예제: https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages

from rich import print as rprint
from langgraph.graph.message import add_messages

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph


class State(TypedDict):
    messages: Annotated[list, add_messages]


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
print('-'*50)
rprint(graph.invoke({"messages": [("user", "hi2")]}))
print('-'*50)
rprint(graph.invoke({"messages": [("user", "hi3"), ("user", "hi4")]}))
# Node chatbot -> state: {'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}, id='0752d0ff-9083-49a6-988a-922edfe4b3eb')]}
# {
#     'messages': [
#         HumanMessage(content='hi', additional_kwargs={}, response_metadata={}, id='0752d0ff-9083-49a6-988a-922edfe4b3eb'),
#         AIMessage(content='Hello', additional_kwargs={}, response_metadata={}, id='85e50f49-04f4-422f-87f0-7872f39541d0')
#     ]
# }
# --------------------------------------------------
# Node chatbot -> state: {'messages': [HumanMessage(content='hi2', additional_kwargs={}, response_metadata={}, id='1db43e49-1082-459e-9f70-840aa766c8c6')]}
# {
#     'messages': [
#         HumanMessage(content='hi2', additional_kwargs={}, response_metadata={}, id='1db43e49-1082-459e-9f70-840aa766c8c6'),
#         AIMessage(content='Hello', additional_kwargs={}, response_metadata={}, id='4293a3fe-5f41-4007-9f61-a92db4bf2ffb')
#     ]
# }
# --------------------------------------------------
# Node chatbot -> state: {'messages': [HumanMessage(content='hi3', additional_kwargs={}, response_metadata={}, id='81205b78-f284-4b8a-9892-b2d14d51a73b'), HumanMessage(content='hi4', additional_kwargs={},
# response_metadata={}, id='b9b70015-a054-40e9-bb10-0654bededddd')]}
# {
#     'messages': [
#         HumanMessage(content='hi3', additional_kwargs={}, response_metadata={}, id='81205b78-f284-4b8a-9892-b2d14d51a73b'),
#         HumanMessage(content='hi4', additional_kwargs={}, response_metadata={}, id='b9b70015-a054-40e9-bb10-0654bededddd'),
#         AIMessage(content='Hello', additional_kwargs={}, response_metadata={}, id='33b00665-89a4-49aa-84f1-a73f2b74db61')
#     ]
# }


### [[add_messages는 message가 누적이 되어야 하는데 node에서는 누적이 아닌 그 시점의 값?]] ###
### invoke의 결과값이 누적이 됨? ###
### 잘 모르겠다. ###