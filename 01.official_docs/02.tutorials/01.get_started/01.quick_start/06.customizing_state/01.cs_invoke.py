# from dotenv import load_dotenv
# load_dotenv()

### [[ "human" node의 역할 ]]
# "human" node는 tool_node의 실행(tool) 여부를 확인 받는 것이 아니라
# tool_node의 tool을 대신 해서 답변을 주는 역할을 함


import custimizing_state as cs
from rich import print as rprint

##################################################################################
### 1. graph invoke 
print('1.', '*'*50)
##################################################################################
user_input = "I need some expert guidance for building this AI agent. Could you request assistance for me?"
config = {"configurable": {"thread_id": "1"}}
# The config is the **second positional argument** to stream() or invoke()!
events = cs.graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 1. **************************************************

### A. ask_human: True --- model=gpt-4o ------------------------------------
# ================================ Human Message =================================

# I need some expert guidance for building this AI agent. Could you request assistance for me?
# ================================== Ai Message ==================================

# [{'text': "Certainly! I'd be happy to request assistance from an expert regarding guidance for building an AI agent. I'll use the RequestAssistance function to escalate your request to an expert who can provide more specialized knowledge and support. Let me do that for you right away.", 'type': 'text'}, {'id': 'toolu_011osMY8MG8WP4oMH6hu1n3x', 'input': {'request': 'The user is seeking expert guidance for building an AI agent. They need specialized knowledge and support in this area.'}, 'name': 'RequestAssistance', 'type': 'tool_use'}]
# Tool Calls:
#   RequestAssistance (toolu_011osMY8MG8WP4oMH6hu1n3x)
#  Call ID: toolu_011osMY8MG8WP4oMH6hu1n3x
#   Args:
#     request: The user is seeking expert guidance for building an AI agent. They need specialized knowledge and support in this area.        
### [[전문가에게 요청]]

### B. ask_human: False --- model=gpt-4o-mini ------------------------------------
# ================================ Human Message =================================

# I need some expert guidance for building this AI agent. Could you request assistance for me?
# select_next_node: False
# ================================== Ai Message ==================================

# What specific guidance or assistance do you need for building your AI agent? Please provide some details so I can relay your request accurately.
### [[AI가 직접 답변하고 종료]]


##################################################################################
### 2. state 조회
print('2.', '*'*50)
##################################################################################
snapshot = cs.graph.get_state(config)
rprint(f'next: {snapshot.next}')
rprint(f'ask_human: {snapshot.values["ask_human"]}')
# 2. **************************************************
### A. ask_human: True ---------------------------------------
# next: ('human',)
# ask_human: True

### [[ 진행 요약 ]]
# 1. response.tool_calls and response.tool_calls[0]["name"] == RequestAssistance.__name__
# => ask_human = True
# 2. select_next_node에서 ask_human이 True이면 human node로 이동
# 3. interrupt_before=["human"] -> human node는 interrupt 설정 되어 있어 interrupt 됨

### B. ask_human: False ---------------------------------------
# next: ()
# ask_human: False

### [[ 진행 요약 ]]
# 1. AI가 tool call을 반환 하지 않음
# => ask_human = False
# 2. AI가 직접 답변하고 종료


####################### ask_human: True 로 진행 #######################

##################################################################################
### 3. 사람이 응답하기
print('3.', '*'*50)
##################################################################################
ai_message = snapshot.values["messages"][-1]
human_response = (
    "We, the experts are here to help! We'd recommend you check out LangGraph to build your agent."
    " It's much more reliable and extensible than simple autonomous agents."
)
tool_message = cs.create_response(human_response, ai_message)
rprint(cs.graph.update_state(config, {"messages": [tool_message]}))
# 3. **************************************************
# {'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1efa88a8-7078-67ac-8002-1d49ee5b7ae2'}}


##################################################################################
### 4. 사람 응답이 추가 되었는지 확인
print('4.', '*'*50)
##################################################################################
rprint(cs.graph.get_state(config).values["messages"])
# 4. **************************************************
# [
#     HumanMessage(
#         content='I need some expert guidance for building this AI agent. Could you request assistance for me?',
#         additional_kwargs={},
#         response_metadata={},
#         id='30f33961-923b-456c-8fa6-f5d4b3fac0e3'
#     ),
#     AIMessage(
#         content='',
#         additional_kwargs={
#             'tool_calls': [
#                 {'id': 'call_dOmNwvDUwr05wBH0ehKSZK63', 'function': {'arguments': '{"request":"I need expert guidance for building an AI agent."}', 'name': 'RequestAssistance'}, 'type': 'function'}   
#             ],
#             'refusal': None
#         },
#         response_metadata={
#             'token_usage': {
#                 'completion_tokens': 24,
#                 'prompt_tokens': 160,
#                 'total_tokens': 184,
#                 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#             },
#             'model_name': 'gpt-4o-2024-08-06',
#             'system_fingerprint': 'fp_45cf54deae',
#             'finish_reason': 'tool_calls',
#             'logprobs': None
#         },
#         id='run-82539bb6-959b-47eb-bb4b-c731d0f5d62c-0',
#         tool_calls=[{'name': 'RequestAssistance', 'args': {'request': 'I need expert guidance for building an AI agent.'}, 'id': 'call_dOmNwvDUwr05wBH0ehKSZK63', 'type': 'tool_call'}],
#         usage_metadata={'input_tokens': 160, 'output_tokens': 24, 'total_tokens': 184, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}      
#     ),
#     ToolMessage(
#         content="We, the experts are here to help! We'd recommend you check out LangGraph to build your agent. It's much more reliable and extensible than simple autonomous agents.",
#         id='7536a8cd-8e5a-44b3-b034-799c22f6b9e9',
#         tool_call_id='call_dOmNwvDUwr05wBH0ehKSZK63'
#     )
# ]


##################################################################################
### 5. graph 재개
print('5.', '*'*50)
##################################################################################
events = cs.graph.stream(None, config, stream_mode="values")
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 5. **************************************************
# ================================= Tool Message =================================

# We, the experts are here to help! We'd recommend you check out LangGraph to build your agent. It's much more reliable and extensible than simple autonomous agents.
# ================================= Tool Message =================================

# We, the experts are here to help! We'd recommend you check out LangGraph to build your agent. It's much more reliable and extensible than simple autonomous agents.
# ================================== Ai Message ==================================

# The experts recommend checking out LangGraph for building your AI agent. They mention that it's more reliable and extensible than simple autonomous agents. If you have more specific questions or need 
# further guidance, feel free to ask!        