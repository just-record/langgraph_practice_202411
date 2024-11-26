import build_basic_chatbot as bbc
from rich import print as rprint

##################################################################################
### 1. graph를 invoke 결과값 전체 조회하기
print('1.', '*'*50)
##################################################################################
result = bbc.graph.invoke({"messages": [{"role": "user", "content": "What do you know about LangGraph?"}]})
rprint(result)
# {
#     'messages': [
#         HumanMessage(content='What do you know about LangGraph?', additional_kwargs={}, response_metadata={}, id='a38f0c42-b9ea-4d34-8bd4-318b3ac9d7d8'),
#         AIMessage(
#             content='As of my last update in October 2023, LangGraph is a framework designed to facilitate the development of applications that leverage large language models (LLMs) in combination with graph-based    
# structures. It typically focuses on enabling more complex interactions and data representations, allowing developers to harness the power of LLMs for tasks that involve structured data and relationships.\n\nLangGraph 
# may offer features like:\n\n1. **Integration with Graph Databases**: It can work with graph databases to store and manage relationships between entities, making it easier to query and manipulate data.\n\n2. **Natural 
# Language Processing (NLP)**: By combining LLMs with graph structures, LangGraph can enhance the understanding of natural language queries and their relationships within a graph context.\n\n3. **Use Cases**: Common    
# applications include knowledge graph construction, recommendation systems, and conversational agents that require an understanding of complex relationships.\n\n4. **APIs and Tools**: It may provide various APIs and   
# tools for developers to seamlessly integrate language understanding with graph data processing.\n\nIf you are interested in specific features, use cases, or recent developments related to LangGraph, I recommend       
# checking the official documentation or resources for the most up-to-date information.',
#             additional_kwargs={'refusal': None},
#             response_metadata={
#                 'token_usage': {
#                     'completion_tokens': 239,
#                     'prompt_tokens': 15,
#                     'total_tokens': 254,
#                     'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                     'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                 },
#                 'model_name': 'gpt-4o-mini-2024-07-18',
#                 'system_fingerprint': 'fp_0705bf87c0',
#                 'finish_reason': 'stop',
#                 'logprobs': None
#             },
#             id='run-79d553c9-ea0f-4f7e-b2ee-4a47a26fbfd2-0',
#             usage_metadata={'input_tokens': 15, 'output_tokens': 239, 'total_tokens': 254, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
#         )
#     ]
# }


##################################################################################
### 2. result['messages']
print('2.', '*'*50)
##################################################################################
rprint(result['messages'][0].content)
print('-'*20)
rprint(result['messages'][1].content[:100])
# What do you know about LangGraph?
# --------------------
# As of my last update in October 2023, LangGraph is not widely recognized in mainstream discussions,


##################################################################################
### 3. result.values(), result.keys()
print('3.', '*'*50)
##################################################################################
for result_value in result.values():
    # rprint(result_value)
    ### 위의 결과가 list여서 for loop로 돌림
    for value in result_value:
        print('+'*20)
        rprint(value.content[:100])
# ++++++++++++++++++++
# What do you know about LangGraph?
# ++++++++++++++++++++
# As of my last knowledge update in October 2023, LangGraph is a tool designed to facilitate the integ        
    
print('-'*20)
    
for result_key in result.keys():
    rprint(result_key)
# messages    