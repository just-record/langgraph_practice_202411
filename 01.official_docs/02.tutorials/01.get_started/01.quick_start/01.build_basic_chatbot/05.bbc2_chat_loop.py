import build_basic_chatbot_2 as bbc2
from rich import print as rprint

##################################################################################
### 1. build_basic_chatbot_2.py로 수정 -> chatbot 노드에 logging 추가 ###
print('1.', '*'*50)
##################################################################################
# def stream_graph_updates(user_input: str):
#     for event in bbc2.graph.stream({"messages": [("user", user_input)]}):
#         for value in event.values():
#             print("Assistant:", value["messages"][-1].content)


# while True:
#     try:
#         user_input = input("User: ")
#         if user_input.lower() in ["quit", "exit", "q"]:
#             print("Goodbye!")
#             break

#         stream_graph_updates(user_input)
#     except:
#         # fallback if input() is not available
#         user_input = "What do you know about LangGraph?"
#         print("User: " + user_input)
#         stream_graph_updates(user_input)
#         break

# 1. **************************************************
# User: hi
# Node chatbot -> state: {'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}, id='be79a43d-86b0-4a05-863d-cb79b4b28d9b')]}
# Node chatbot -> llm_response: content='Hello! How can I assist you today?' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 8, 'total_tokens': 17,        
# 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
# 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_0ba0d124f1', 'finish_reason': 'stop', 'logprobs': None} id='run-bfafdf0e-72f3-4948-ba04-399bd1855ea0-0' usage_metadata={'input_tokens': 8,
# 'output_tokens': 9, 'total_tokens': 17, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# Assistant: Hello! How can I assist you today?
# User: My name is Jildong Hong
# Node chatbot -> state: {'messages': [HumanMessage(content='My name is Jildong Hong', additional_kwargs={}, response_metadata={}, id='a09cb2b4-3bc1-4e58-a962-637d5dbbc845')]}
# Node chatbot -> llm_response: content='Nice to meet you, Jildong Hong! How can I assist you today?' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 14, 
# 'total_tokens': 31, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0,
# 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_0ba0d124f1', 'finish_reason': 'stop', 'logprobs': None} id='run-7c40ae2a-718c-438e-b964-b49ccf98fb74-0'
# usage_metadata={'input_tokens': 14, 'output_tokens': 17, 'total_tokens': 31, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# Assistant: Nice to meet you, Jildong Hong! How can I assist you today?
# User: What's my name?
# Node chatbot -> state: {'messages': [HumanMessage(content="What's my name?", additional_kwargs={}, response_metadata={}, id='54b0f4aa-21df-4ce5-b9ec-f9431e9713c0')]}
# Node chatbot -> llm_response: content="I don't have access to personal information, so I don't know your name unless you tell me. How can I assist you today?" additional_kwargs={'refusal': None}
# response_metadata={'token_usage': {'completion_tokens': 26, 'prompt_tokens': 11, 'total_tokens': 37, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0,
# 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_3de1288069', 'finish_reason': 'stop', 'logprobs': 
# None} id='run-4009f8b9-d454-45f4-97e0-d84d180307b3-0' usage_metadata={'input_tokens': 11, 'output_tokens': 26, 'total_tokens': 37, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details':
# {'audio': 0, 'reasoning': 0}}
# Assistant: I don't have access to personal information, so I don't know your name unless you tell me. How can I assist you today?
# User: q
# Goodbye!

### [[state에 최종 message만 있음]] ###


##################################################################################
### 2. graph.stream을 invoke로 변경 - stream은 message가 최종 하나만 있음 - 1.번 주석 처리
print('2.', '*'*50)
##################################################################################
def stream_graph_updates(user_input: str):
    messages = bbc2.graph.invoke({"messages": [("user", user_input)]})['messages']
    print(f'Assistant: {messages[-1].content}')


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break
    
# 2. **************************************************
# User: hi
# Node chatbot -> state: {'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}, id='f2de0fd5-a80c-4a3b-8fa5-aba4d28b5a0c')]}
# Node chatbot -> llm_response: content='Hello! How can I assist you today?' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 8, 'total_tokens': 17, 
# 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
# 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_9b78b61c52', 'finish_reason': 'stop', 'logprobs': None} id='run-68fce384-363b-4401-85a3-6278b808f260-0' usage_metadata={'input_tokens': 8,
# 'output_tokens': 9, 'total_tokens': 17, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# Assistant: Hello! How can I assist you today?
# User: My name is Jildong Hong
# Node chatbot -> state: {'messages': [HumanMessage(content='My name is Jildong Hong', additional_kwargs={}, response_metadata={}, id='80ce1e47-5213-4e41-b71f-c796dd253b6a')]}
# Node chatbot -> llm_response: content='Nice to meet you, Jildong Hong! How can I assist you today?' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 14, 
# 'total_tokens': 31, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0,
# 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_0ba0d124f1', 'finish_reason': 'stop', 'logprobs': None} id='run-b0c3185f-7428-4b29-8dd7-5f2495cea5ca-0'
# usage_metadata={'input_tokens': 14, 'output_tokens': 17, 'total_tokens': 31, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# Assistant: Nice to meet you, Jildong Hong! How can I assist you today?
# User: What's my name
# Node chatbot -> state: {'messages': [HumanMessage(content="What's my name", additional_kwargs={}, response_metadata={}, id='4ddea636-13e0-4a6f-99e9-ab20f11dc420')]}
# Node chatbot -> llm_response: content="I'm sorry, but I don't have access to personal information about you unless you share it with me. What would you like me to call you?" additional_kwargs={'refusal': None} 
# response_metadata={'token_usage': {'completion_tokens': 29, 'prompt_tokens': 10, 'total_tokens': 39, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0,
# 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_0ba0d124f1', 'finish_reason': 'stop', 'logprobs': 
# None} id='run-647f6df3-dfe5-4af5-a1bb-2a10212b4ce4-0' usage_metadata={'input_tokens': 10, 'output_tokens': 29, 'total_tokens': 39, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details':
# {'audio': 0, 'reasoning': 0}}
# Assistant: I'm sorry, but I don't have access to personal information about you unless you share it with me. What would you like me to call you?
# User: q
# Goodbye!    


### [[invoke도 state에 최종 message만 있음]] ###
### [[Node에 입력되는 state는 누적? 이 아닌 그 시점의? 값만 있음]] ###