# from dotenv import load_dotenv
# load_dotenv()

import manually_update_state as mus
from rich import print as rprint

##################################################################################
### 1. graph invoke -> tools node에서 interrupt 됨
print('1.', '*'*50)
##################################################################################
user_input = "I'm learning LangGraph. Could you do some research on it for me?"
config = {"configurable": {"thread_id": "1"}}
# The config is the **second positional argument** to stream() or invoke()!
events = mus.graph.stream({"messages": [("user", user_input)]}, config, stream_mode="values")
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 1. **************************************************
# ================================ Human Message =================================

# I'm learning LangGraph. Could you do some research on it for me?
# ================================== Ai Message ==================================
# Tool Calls:
#   tavily_search_results_json (call_EtWmAtxPlGyv99cZyJgkSkFR)
#  Call ID: call_EtWmAtxPlGyv99cZyJgkSkFR
#   Args:
#     query: LangGraph        
        

##################################################################################
### 2. 멈춘 상태값 조회
print('2.', '*'*50)
##################################################################################
snapshot = mus.graph.get_state(config)
existing_message = snapshot.values["messages"][-1]
existing_message.pretty_print()
# 2. **************************************************
# ================================== Ai Message ==================================
# Tool Calls:
#   tavily_search_results_json (call_Ert9styGLTS8i7oECHLjMN1y)
#  Call ID: call_Ert9styGLTS8i7oECHLjMN1y
#   Args:
#     query: LangGraph


##################################################################################
### 3. update_state() 로 상태값 업데이트
print('3.', '*'*50)
##################################################################################
from langchain_core.messages import AIMessage, ToolMessage

answer = (
    "LangGraph is a library for building stateful, multi-actor applications with LLMs."
)
new_messages = [
    # The LLM API expects some ToolMessage to match its tool call. We'll satisfy that here.
    ToolMessage(content=answer, tool_call_id=existing_message.tool_calls[0]["id"]),
    # And then directly "put words in the LLM's mouth" by populating its response.
    AIMessage(content=answer),
]

new_messages[-1].pretty_print()
mus.graph.update_state(
    # Which state to update
    config,
    # The updated values to provide. The messages in our `State` are "append-only", meaning this will be appended
    # to the existing state. We will review how to update existing messages in the next section!
    {"messages": new_messages},
)

print("\n\nLast 2 messages;")
print(mus.graph.get_state(config).values["messages"][-2:])
# 3. **************************************************
# ================================== Ai Message ==================================

# LangGraph is a library for building stateful, multi-actor applications with LLMs.

# Last 2 messages;
# [
#   ToolMessage(content='LangGraph is a library for building stateful, multi-actor applications with LLMs.', id='438402de-2b68-4390-89d9-a6d20baf6716', tool_call_id='call_gn2usLaIYstFsRrqkGS8J1XP'), 
#   AIMessage(content='LangGraph is a library for building stateful, multi-actor applications with LLMs.', additional_kwargs={}, response_metadata={}, id='adcd8398-074d-4b88-a9e4-40afd3c73428')
# ]


rprint(mus.graph.get_state(config))
# StateSnapshot(
#     values={
#         'messages': [
#             HumanMessage(content="I'm learning LangGraph. Could you do some research on it for me?", additional_kwargs={}, response_metadata={}, id='1e695d25-5897-4897-a211-5e4750f94e0d'),
#             AIMessage(
#                 content='',
#                 additional_kwargs={
#                     'tool_calls': [{'id': 'call_RAE85qmjpv7rJJPHCgYD54YN', 'function': {'arguments': '{"query":"LangGraph"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}],
#                     'refusal': None
#                 },
#                 response_metadata={
#                     'token_usage': {
#                         'completion_tokens': 19,
#                         'prompt_tokens': 94,
#                         'total_tokens': 113,
#                         'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                         'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                     },
#                     'model_name': 'gpt-4o-mini-2024-07-18',
#                     'system_fingerprint': 'fp_3de1288069',
#                     'finish_reason': 'tool_calls',
#                     'logprobs': None
#                 },
#                 id='run-43d25c41-a2ab-483a-bd48-8b65f5b434df-0',
#                 tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'LangGraph'}, 'id': 'call_RAE85qmjpv7rJJPHCgYD54YN', 'type': 'tool_call'}],
#                 usage_metadata={
#                     'input_tokens': 94,
#                     'output_tokens': 19,
#                     'total_tokens': 113,
#                     'input_token_details': {'audio': 0, 'cache_read': 0},
#                     'output_token_details': {'audio': 0, 'reasoning': 0}
#                 }
#             ),
#             ToolMessage(
#                 content='LangGraph is a library for building stateful, multi-actor applications with LLMs.',
#                 id='c80ec329-e381-4fa8-92f3-cbfe0278b605',
#                 tool_call_id='call_RAE85qmjpv7rJJPHCgYD54YN'
#             ),
#             AIMessage(
#                 content='LangGraph is a library for building stateful, multi-actor applications with LLMs.',
#                 additional_kwargs={},
#                 response_metadata={},
#                 id='b0a8f78d-8137-4b17-82cf-1ccc3bda03be'
#             )
#         ]
#     },
#     next=(),
#     config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1efa7e68-935d-6d8d-8002-2f2dfd34b525'}},
#     metadata={
#         'source': 'update',
#         'writes': {
#             'chatbot': {
#                 'messages': [
#                     ToolMessage(
#                         content='LangGraph is a library for building stateful, multi-actor applications with LLMs.',
#                         id='c80ec329-e381-4fa8-92f3-cbfe0278b605',
#                         tool_call_id='call_RAE85qmjpv7rJJPHCgYD54YN'
#                     ),
#                     AIMessage(
#                         content='LangGraph is a library for building stateful, multi-actor applications with LLMs.',
#                         additional_kwargs={},
#                         response_metadata={},
#                         id='b0a8f78d-8137-4b17-82cf-1ccc3bda03be'
#                     )
#                 ]
#             }
#         },
#         'thread_id': '1',
#         'step': 2,
#         'parents': {}
#     },
#     created_at='2024-11-21T08:56:45.810010+00:00',
#     parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1efa7e68-9334-657b-8001-0da20789c4e9'}},
#     tasks=()
# )





##################################################################################
### 4. 시작하는 node를 지정하여 상태값 update
print('4.', '*'*50)
##################################################################################
mus.graph.update_state(
    config,
    {"messages": [AIMessage(content="I'm an AI expert!")]},
    # Which node for this function to act as. It will automatically continue
    # processing as if this node just ran.
    as_node="chatbot",
)

snapshot = mus.graph.get_state(config)
rprint(snapshot.values["messages"][-3:])
rprint(snapshot.next)
# 4. **************************************************
# [
#     ToolMessage(content='LangGraph is a library for building stateful, multi-actor applications with LLMs.', id='99f3b7c8-e6ea-409c-9e40-28078c43b7b3', tool_call_id='call_YRBMGavWEg7lxufsIs8iu9rt'),  
#     AIMessage(content='LangGraph is a library for building stateful, multi-actor applications with LLMs.', additional_kwargs={}, response_metadata={}, id='6e8f3a70-26ed-4309-9929-9566047a6054'),      
#     AIMessage(content="I'm an AI expert!", additional_kwargs={}, response_metadata={}, id='4d4bfd0f-5bae-45f1-9c8a-7b093b79fbb8')
# ]
# ()

### [[ chatbot node에서 시작하여 AIMessage 추가 ]] ###
### [[ tool_call이 없어서 tool_node로 가지 않고 END로 이동 ]] ###
### [[ END로 이동 하여 next가 없음]] ###