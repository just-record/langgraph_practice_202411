# tools_condition
# <https://langchain-ai.github.io/langgraph/reference/prebuilt/?h=tools+condition#langgraph.prebuilt.tool_node.tools_condition>

###########################################
### "tools" node 이름을 변경하면 오류 발생 ###
###########################################


from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages

from typing import TypedDict, Annotated

from rich import print as rprint

@tool
def divide(a: float, b: float) -> int:
    """Return a / b."""
    return a / b

llm = ChatOpenAI(model="gpt-4o-mini")
tools = [divide]

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)
### 1. 예제 소스 코드 그대로 실행 하기
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.add_node("chatbot", lambda state: {"messages":llm.bind_tools(tools).invoke(state['messages'])})
graph_builder.add_edge("tools", "chatbot")
### 2. "tools" node 이름을 변경하여 실행 하기
# graph_builder.add_node("tools_devide", ToolNode(tools))
# graph_builder.add_node("chatbot", lambda state: {"messages":llm.bind_tools(tools).invoke(state['messages'])})
# graph_builder.add_edge("tools", "chatbot")
##############################################

graph_builder.add_conditional_edges(
    "chatbot", tools_condition
)
graph_builder.set_entry_point("chatbot")
graph = graph_builder.compile()


##################################################################################
### 1. 예세 소스 코드 그대로 실행 하기
print('1.', '*'*50)
##################################################################################    
# result = graph.invoke({"messages": {"role": "user", "content": "What's 329993 divided by 13662?"}})
# rprint(result)
# {
#     'messages': [
#         HumanMessage(content="What's 329993 divided by 13662?", additional_kwargs={}, response_metadata={}, id='1cf8bad7-b1c9-4a01-8bdc-451bafe40919'),
#         AIMessage(
#             content='',
#             additional_kwargs={'tool_calls': [{'id': 'call_uvJIYxa8zXSBoFBo0KOvkZsp', 'function': {'arguments': '{"a":329993,"b":13662}', 'name': 'divide'}, 'type': 'function'}], 'refusal': None},    
#             response_metadata={
#                 'token_usage': {
#                     'completion_tokens': 19,
#                     'prompt_tokens': 55,
#                     'total_tokens': 74,
#                     'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                     'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                 },
#                 'model_name': 'gpt-4o-mini-2024-07-18',
#                 'system_fingerprint': 'fp_0705bf87c0',
#                 'finish_reason': 'tool_calls',
#                 'logprobs': None
#             },
#             id='run-7e6e2df0-88a5-4c1b-800a-d2c0d3b64251-0',
#             tool_calls=[{'name': 'divide', 'args': {'a': 329993, 'b': 13662}, 'id': 'call_uvJIYxa8zXSBoFBo0KOvkZsp', 'type': 'tool_call'}],
#             usage_metadata={'input_tokens': 55, 'output_tokens': 19, 'total_tokens': 74, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}    
#         ),
#         ToolMessage(content='24.15407700190309', name='divide', id='be0db46f-abfd-45a3-b0d5-016f9cba0a75', tool_call_id='call_uvJIYxa8zXSBoFBo0KOvkZsp'),
#         AIMessage(
#             content='329993 divided by 13662 is approximately 24.15.',
#             additional_kwargs={'refusal': None},
#             response_metadata={
#                 'token_usage': {
#                     'completion_tokens': 15,
#                     'prompt_tokens': 88,
#                     'total_tokens': 103,
#                     'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                     'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                 },
#                 'model_name': 'gpt-4o-mini-2024-07-18',
#                 'system_fingerprint': 'fp_0705bf87c0',
#                 'finish_reason': 'stop',
#                 'logprobs': None
#             },
#             id='run-69e6b819-b49d-47b0-ac69-5b72d5afcffc-0',
#             usage_metadata={'input_tokens': 88, 'output_tokens': 15, 'total_tokens': 103, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}   
#         )
#     ]
# }


##################################################################################
### 2. "tools" node 이름을 변경하여 실행 하기
print('2.', '*'*50)
##################################################################################    
result = graph.invoke({"messages": {"role": "user", "content": "What's 329993 divided by 13662?"}})
rprint(result)
### [[오류 발생]] ###
# ValueError: Found edge starting at unknown node 'tools'