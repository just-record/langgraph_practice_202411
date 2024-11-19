import build_basic_chatbot as bbc

# pip install rich
from rich import print as rprint

##################################################################################
### 1. graph를 invoke 하기
### 입력값을 {"messages": [{"role": "", "content": ""}]} 형태로 넣기
print('1', '*'*50)
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
### 2. graph를 invoke 하기
### 입력값을 {"messages": [""]} 형태로 넣기
print('2', '*'*50)
##################################################################################
result = bbc.graph.invoke({"messages": ["What do you know about LangGraph?"]})
rprint(result)
# 위와 동일한 결과


##################################################################################
### 3. graph를 invoke 하기
### 입력값을 "" 형태로 넣기
print('3', '*'*50)
##################################################################################
result = bbc.graph.invoke("What do you know about LangGraph?")
rprint(result)
### [[오류 발생]] ###
# langgraph.errors.InvalidUpdateError: Expected dict, got What do you know about LangGraph?
# For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE

### graph의 입력값은 dictionary type로 넣어야 하는 듯. ###
### node의 입력이 state이므로 state와 동일한 type이어햐 할 듯  ###