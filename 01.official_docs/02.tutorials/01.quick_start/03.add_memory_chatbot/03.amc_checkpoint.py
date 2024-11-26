### Checkpoint: State snapshot at a given point in time.
# <https://langchain-ai.github.io/langgraph/reference/checkpoints/?query=checkpoint#langgraph.checkpoint.base.Checkpoint>

### Checkpointer: Checkpointer used to save and load graph state. Defaults to None. 
# <https://langchain-ai.github.io/langgraph/reference/checkpoints/?query=checkpoint>

import add_memory_chatbot as amc
from rich import print as rprint

config = {"configurable": {"thread_id": "1"}}

##################################################################################
### 1. config만 설정하고 아무 것도 호출하지 않은 상태
print('1.', '*'*50)
##################################################################################   
snapshot = amc.graph.get_state(config)
rprint(snapshot)
# StateSnapshot(values={}, next=(), config={'configurable': {'thread_id': '1'}}, metadata=None, created_at=None, parent_config=None, tasks=())

user_input = "Hi there! My name is Will."


events = amc.graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)
for event in events:
    event["messages"][-1].pretty_print()

##################################################################################
### 2. thread_id: 1 -> 이름을 말하면서 인사를 호출 한 상태
print('2.', '*'*50)
##################################################################################   
snapshot = amc.graph.get_state(config)
rprint(snapshot)    
# 2. **************************************************
# StateSnapshot(
#     values={
#         'messages': [
#             HumanMessage(content='Hi there! My name is Will.', additional_kwargs={}, response_metadata={}, id='508f2c2b-b15e-4aee-9453-9e5672eff8cb'),
#             AIMessage(
#                 content='Hi Will! How can I assist you today?',
#                 additional_kwargs={'refusal': None},
#                 response_metadata={
#                     'token_usage': {
#                         'completion_tokens': 11,
#                         'prompt_tokens': 87,
#                         'total_tokens': 98,
#                         'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                         'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                     },
#                     'model_name': 'gpt-4o-mini-2024-07-18',
#                     'system_fingerprint': 'fp_0705bf87c0',
#                     'finish_reason': 'stop',
#                     'logprobs': None
#                 },
#                 id='run-fac2d437-115e-47ee-bd96-6160c266b288-0',
#                 usage_metadata={
#                     'input_tokens': 87,
#                     'output_tokens': 11,
#                     'total_tokens': 98,
#                     'input_token_details': {'audio': 0, 'cache_read': 0},
#                     'output_token_details': {'audio': 0, 'reasoning': 0}
#                 }
#             )
#         ]
#     },
#     next=(),
#     config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1efa7b2a-0df2-6d7a-8001-fbbcc2a98c40'}},
#     metadata={
#         'source': 'loop',
#         'writes': {
#             'chatbot': {
#                 'messages': [
#                     AIMessage(
#                         content='Hi Will! How can I assist you today?',
#                         additional_kwargs={'refusal': None},
#                         response_metadata={
#                             'token_usage': {
#                                 'completion_tokens': 11,
#                                 'prompt_tokens': 87,
#                                 'total_tokens': 98,
#                                 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                                 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                             },
#                             'model_name': 'gpt-4o-mini-2024-07-18',
#                             'system_fingerprint': 'fp_0705bf87c0',
#                             'finish_reason': 'stop',
#                             'logprobs': None
#                         },
#                         id='run-fac2d437-115e-47ee-bd96-6160c266b288-0',
#                         usage_metadata={
#                             'input_tokens': 87,
#                             'output_tokens': 11,
#                             'total_tokens': 98,
#                             'input_token_details': {'audio': 0, 'cache_read': 0},
#                             'output_token_details': {'audio': 0, 'reasoning': 0}
#                         }
#                     )
#                 ]
#             }
#         },
#         'thread_id': '1',
#         'step': 1,
#         'parents': {}
#     },
#     created_at='2024-11-21T02:45:11.677273+00:00',
#     parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1efa7b2a-05f6-6bdb-8000-1c7a45db95e9'}},
#     tasks=()
# )
    

user_input = "Remember my name?"

events = amc.graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)
for event in events:
    event["messages"][-1].pretty_print()
##################################################################################
### 3. thread_id: 1 -> 내 이름을 기억하는지 물어본 상태
print('3.', '*'*50)
##################################################################################       
snapshot = amc.graph.get_state(config)
rprint(snapshot)
# StateSnapshot(
#     values={
#         'messages': [
#             HumanMessage(content='Hi there! My name is Will.', additional_kwargs={}, response_metadata={}, id='508f2c2b-b15e-4aee-9453-9e5672eff8cb'),
#             AIMessage(
#                 content='Hi Will! How can I assist you today?',
#                 additional_kwargs={'refusal': None},
#                 response_metadata={
#                     'token_usage': {
#                         'completion_tokens': 11,
#                         'prompt_tokens': 87,
#                         'total_tokens': 98,
#                         'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                         'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                     },
#                     'model_name': 'gpt-4o-mini-2024-07-18',
#                     'system_fingerprint': 'fp_0705bf87c0',
#                     'finish_reason': 'stop',
#                     'logprobs': None
#                 },
#                 id='run-fac2d437-115e-47ee-bd96-6160c266b288-0',
#                 usage_metadata={
#                     'input_tokens': 87,
#                     'output_tokens': 11,
#                     'total_tokens': 98,
#                     'input_token_details': {'audio': 0, 'cache_read': 0},
#                     'output_token_details': {'audio': 0, 'reasoning': 0}
#                 }
#             ),
#             HumanMessage(content='Remember my name?', additional_kwargs={}, response_metadata={}, id='2325321d-c686-4acf-b9a1-4a65efaebcff'),
#             AIMessage(
#                 content='Yes, I remember your name is Will! How can I help you today?',
#                 additional_kwargs={'refusal': None},
#                 response_metadata={
#                     'token_usage': {
#                         'completion_tokens': 17,
#                         'prompt_tokens': 109,
#                         'total_tokens': 126,
#                         'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                         'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                     },
#                     'model_name': 'gpt-4o-mini-2024-07-18',
#                     'system_fingerprint': 'fp_0705bf87c0',
#                     'finish_reason': 'stop',
#                     'logprobs': None
#                 },
#                 id='run-3456c60e-2bd2-4842-b602-f5a1bbb6c122-0',
#                 usage_metadata={
#                     'input_tokens': 109,
#                     'output_tokens': 17,
#                     'total_tokens': 126,
#                     'input_token_details': {'audio': 0, 'cache_read': 0},
#                     'output_token_details': {'audio': 0, 'reasoning': 0}
#                 }
#             )
#         ]
#     },
#     next=(),
#     config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1efa7b2a-15a0-661d-8004-a5e871080384'}},
#     metadata={
#         'source': 'loop',
#         'writes': {
#             'chatbot': {
#                 'messages': [
#                     AIMessage(
#                         content='Yes, I remember your name is Will! How can I help you today?',
#                         additional_kwargs={'refusal': None},
#                         response_metadata={
#                             'token_usage': {
#                                 'completion_tokens': 17,
#                                 'prompt_tokens': 109,
#                                 'total_tokens': 126,
#                                 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                                 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                             },
#                             'model_name': 'gpt-4o-mini-2024-07-18',
#                             'system_fingerprint': 'fp_0705bf87c0',
#                             'finish_reason': 'stop',
#                             'logprobs': None
#                         },
#                         id='run-3456c60e-2bd2-4842-b602-f5a1bbb6c122-0',
#                         usage_metadata={
#                             'input_tokens': 109,
#                             'output_tokens': 17,
#                             'total_tokens': 126,
#                             'input_token_details': {'audio': 0, 'cache_read': 0},
#                             'output_token_details': {'audio': 0, 'reasoning': 0}
#                         }
#                     )
#                 ]
#             }
#         },
#         'thread_id': '1',
#         'step': 4,
#         'parents': {}
#     },
#     created_at='2024-11-21T02:45:12.482358+00:00',
#     parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1efa7b2a-0e39-6a41-8003-2fc13ffe2cc2'}},
#     tasks=()
# )


user_input = "Remember my name?"

# The only difference is we change the `thread_id` here to "2" instead of "1"
events = amc.graph.stream(
    {"messages": [("user", user_input)]},
    {"configurable": {"thread_id": "2"}},
    stream_mode="values",
)
for event in events:
    event["messages"][-1].pretty_print()
##################################################################################
### 4. thread_id: 2 -> thread_id를 변경 -> 내 이름을 기억하는지 물어본 상태
print('4.', '*'*50)
##################################################################################       
snapshot = amc.graph.get_state({"configurable": {"thread_id": "2"}})
rprint(snapshot)        
# 4. **************************************************
# StateSnapshot(
#     values={
#         'messages': [
#             HumanMessage(content='Remember my name?', additional_kwargs={}, response_metadata={}, id='07a887df-8551-4699-82fd-8f8397ba51c2'),
#             AIMessage(
#                 content='I don’t have the ability to remember personal information or past interactions. However, I’m here to help you with any questions or tasks you have right now! What would you 
# like to know or do today?',
#                 additional_kwargs={'refusal': None},
#                 response_metadata={
#                     'token_usage': {
#                         'completion_tokens': 43,
#                         'prompt_tokens': 83,
#                         'total_tokens': 126,
#                         'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                         'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                     },
#                     'model_name': 'gpt-4o-mini-2024-07-18',
#                     'system_fingerprint': 'fp_0705bf87c0',
#                     'finish_reason': 'stop',
#                     'logprobs': None
#                 },
#                 id='run-8fa81924-ec27-44f0-9688-a105d66768ff-0',
#                 usage_metadata={
#                     'input_tokens': 83,
#                     'output_tokens': 43,
#                     'total_tokens': 126,
#                     'input_token_details': {'audio': 0, 'cache_read': 0},
#                     'output_token_details': {'audio': 0, 'reasoning': 0}
#                 }
#             )
#         ]
#     },
#     next=(),
#     config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1efa7b36-9f43-6b81-8001-09e38109a116'}},
#     metadata={
#         'source': 'loop',
#         'writes': {
#             'chatbot': {
#                 'messages': [
#                     AIMessage(
#                         content='I don’t have the ability to remember personal information or past interactions. However, I’m here to help you with any questions or tasks you have right now! What     
# would you like to know or do today?',
#                         additional_kwargs={'refusal': None},
#                         response_metadata={
#                             'token_usage': {
#                                 'completion_tokens': 43,
#                                 'prompt_tokens': 83,
#                                 'total_tokens': 126,
#                                 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                                 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                             },
#                             'model_name': 'gpt-4o-mini-2024-07-18',
#                             'system_fingerprint': 'fp_0705bf87c0',
#                             'finish_reason': 'stop',
#                             'logprobs': None
#                         },
#                         id='run-8fa81924-ec27-44f0-9688-a105d66768ff-0',
#                         usage_metadata={
#                             'input_tokens': 83,
#                             'output_tokens': 43,
#                             'total_tokens': 126,
#                             'input_token_details': {'audio': 0, 'cache_read': 0},
#                             'output_token_details': {'audio': 0, 'reasoning': 0}
#                         }
#                     )
#                 ]
#             }
#         },
#         'thread_id': '2',
#         'step': 1,
#         'parents': {}
#     },
#     created_at='2024-11-21T02:50:49.037299+00:00',
#     parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1efa7b36-91ae-6392-8000-ec403f11421d'}},
#     tasks=()
# )