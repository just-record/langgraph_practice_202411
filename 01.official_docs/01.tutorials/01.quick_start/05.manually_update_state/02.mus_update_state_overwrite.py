# from dotenv import load_dotenv
# load_dotenv()

import manually_update_state as mus
from rich import print as rprint


##################################################################################
### 1. graph invoke -> tools node에서 interrupt 됨
print('1.', '*'*50)
##################################################################################
user_input = "I'm learning LangGraph. Could you do some research on it for me?"
config = {"configurable": {"thread_id": "2"}}  # we'll use thread_id = 2 here
events = mus.graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 1. **************************************************
# ================================ Human Message =================================

# I'm learning LangGraph. Could you do some research on it for me?
# ================================== Ai Message ==================================
# Tool Calls:
#   tavily_search_results_json (call_IH7Id83n0Jy8dDZH56tzK4GG)
#  Call ID: call_IH7Id83n0Jy8dDZH56tzK4GG
#   Args:
#     query: LangGraph        
        

##################################################################################
### 2. 이전 message의 id를 사용하여 message 업데이트(overwrite)
print('2.', '*'*50)
##################################################################################        
from langchain_core.messages import AIMessage

snapshot = mus.graph.get_state(config)
existing_message = snapshot.values["messages"][-1]
print("Original")
print("Message ID", existing_message.id)
print(existing_message.tool_calls[0])
new_tool_call = existing_message.tool_calls[0].copy()
new_tool_call["args"]["query"] = "LangGraph human-in-the-loop workflow"
new_message = AIMessage(
    content=existing_message.content,
    tool_calls=[new_tool_call],
    # Important! The ID is how LangGraph knows to REPLACE the message in the state rather than APPEND this messages
    id=existing_message.id,
)

print("Updated")
print(new_message.tool_calls[0])
print("Message ID", new_message.id)
mus.graph.update_state(config, {"messages": [new_message]})

print("\n\nTool calls")
mus.graph.get_state(config).values["messages"][-1].tool_calls        
# 2. **************************************************
# Original
# Message ID run-5c293db7-ca12-49ec-9a86-bb2a8779daeb-0
# {'name': 'tavily_search_results_json', 'args': {'query': 'LangGraph'}, 'id': 'call_IH7Id83n0Jy8dDZH56tzK4GG', 'type': 'tool_call'}
# Updated
# {'name': 'tavily_search_results_json', 'args': {'query': 'LangGraph human-in-the-loop workflow'}, 'id': 'call_IH7Id83n0Jy8dDZH56tzK4GG', 'type': 'tool_call'}
# Message ID run-5c293db7-ca12-49ec-9a86-bb2a8779daeb-0

# Tool calls


##################################################################################
### 3. interrupt 된 상태에서 none을 전달하여 graph 진행 시키기
# overwrite 된 message로 tool call을 실행 함
print('3.', '*'*50)
##################################################################################        
events = mus.graph.stream(None, config, stream_mode="values")
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 3. **************************************************
# ================================== Ai Message ==================================
# Tool Calls:
#   tavily_search_results_json (call_uD6l1Qr9Zgk0xTd6ig5pYHgW)
#  Call ID: call_uD6l1Qr9Zgk0xTd6ig5pYHgW
#   Args:
#     query: LangGraph human-in-the-loop workflow
# ================================= Tool Message =================================
# Name: tavily_search_results_json

# [{"url": "https://www.youtube.com/watch?v=9BPCV5TYPmg", "content": "In this video, I'll show you how to handle persistence with LangGraph, enabling a unique Human-in-the-Loop workflow. This approach allows a human to grant an"}, {"url": "https://medium.com/@harishreddykondapalli/building-a-human-in-the-loop-movie-recommendation-system-with-langgraph-44541f151e80", "content": "Building a Human-in-the-Loop Movie Recommendation System with LangGraph | by Harish Kondapalli | Nov, 2024 | Medium In this post, I'll walk you through using LangGraph to create a movie recommendation system that allows users to refine their preferences in real-time. Each agent performs a specific function in the recommendation process, allowing the system to ask users for input, filter movie suggestions based on genre, and provide tailored recommendations. LangGraph provides a robust, flexible framework for building human-in-the-loop recommendation systems that adapt to user input. Whether for movie recommendations or other interactive applications, LangGraph’s multi-agent, graph-based design enables developers to create personalized, scalable solutions that respond in real-time to individual preferences."}] 
# ================================== Ai Message ==================================

# Here are some resources and insights about LangGraph, particularly focusing on its human-in-the-loop workflow:

# 1. **YouTube Video on Persistence with LangGraph**: This video demonstrates how to handle persistence within LangGraph, emphasizing a unique human-in-the-loop workflow. The approach allows a human to 
# interact and grant inputs, making the system more responsive and adaptable. You can watch it [here](https://www.youtube.com/watch?v=9BPCV5TYPmg).
# ... 생략


##################################################################################
### 4. 수정된 상태를 모두 기억하는지 조회
print('4.', '*'*50)
##################################################################################        
events = mus.graph.stream(
    {
        "messages": (
            "user",
            "Remember what I'm learning about?",
        )
    },
    config,
    stream_mode="values",
)
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 4. **************************************************
# ================================ Human Message =================================

# Remember what I'm learning about?
# ================================== Ai Message ==================================

# Yes, you mentioned that you're learning about LangGraph, particularly its application in creating human-in-the-loop workflows. If you have any specific aspects you want to explore further or questions about LangGraph, feel free to let me know!        


##################################################################################
### 5. state 조회
print('5.', '*'*50)
##################################################################################        
snapshot = mus.graph.get_state(config)
rprint(snapshot)
# 5. **************************************************
# StateSnapshot(
#     values={
#         'messages': [
#             HumanMessage(content="I'm learning LangGraph. Could you do some research on it for me?", additional_kwargs={}, response_metadata={}, id='2c10b2b1-2e19-42e0-bf3c-d04f98877f3e'),
#             AIMessage(
#                 content='',
#                 additional_kwargs={},
#                 response_metadata={},
#                 id='run-9ca41870-4901-4fbb-8e70-9bd9b9990a9f-0',
#                 tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'LangGraph human-in-the-loop workflow'}, 'id': 'call_9kPcHJ8t426E7gyeYkkymrZu', 'type': 'tool_call'}]
#             ),
#             ToolMessage(
#                 content='[{"url": "https://www.youtube.com/watch?v=9BPCV5TYPmg", "content": "In this video, I\'ll show you how to handle persistence with LangGraph, enabling a unique Human-in-the-Loopworkflow. This approach allows a human to grant an"}, {"url": "https://medium.com/@kbdhunga/implementing-human-in-the-loop-with-langgraph-ccfde023385c", "content": "In this article, we will explore   
# how the human-in-the-loop mechanism works in LangGraph with a simple example. In this example, we introduce a breakpoint before the tools are executed (action) to"}]',
#                 name='tavily_search_results_json',
#                 id='dc3d04b1-1698-4450-b48c-1cbe7e3a858c',
#                 tool_call_id='call_9kPcHJ8t426E7gyeYkkymrZu',
#                 artifact={
#                     'query': 'LangGraph human-in-the-loop workflow',
#                     'follow_up_questions': None,
#                     'answer': None,
#                     'images': [],
#                     'results': [
#                         {
#                             'title': 'LangGraph - Persistence & Human-in-the-Loop Workflow - YouTube',
#                             'url': 'https://www.youtube.com/watch?v=9BPCV5TYPmg',
#                             'content': "In this video, I'll show you how to handle persistence with LangGraph, enabling a unique Human-in-the-Loop workflow. This approach allows a human to grant an", 
#                             'score': 0.9992706,
#                             'raw_content': None
#                         },
#                         {
#                             'title': 'Implementing Human-in-the-Loop with LangGraph - Medium',
#                             'url': 'https://medium.com/@kbdhunga/implementing-human-in-the-loop-with-langgraph-ccfde023385c',
#                             'content': 'In this article, we will explore how the human-in-the-loop mechanism works in LangGraph with a simple example. In this example, we introduce a breakpoint beforethe tools are executed (action) to',
#                             'score': 0.99729556,
#                             'raw_content': None
#                         }
#                     ],
#                     'response_time': 2.53
#                 }
#             ),
#             AIMessage(
#                 content="Here are some resources that can help you learn about LangGraph and its human-in-the-loop workflow:\n\n1. **Video Tutorial**: There's a [YouTube 
# video](https://www.youtube.com/watch?v=9BPCV5TYPmg) that demonstrates how to handle persistence with LangGraph, showcasing a unique human-in-the-loop workflow. This approach allows a human to grant anapproval or make decisions at certain points in the process.\n\n2. **Article on Implementation**: A detailed [Medium 
# article](https://medium.com/@kbdhunga/implementing-human-in-the-loop-with-langgraph-ccfde023385c) explains how the human-in-the-loop mechanism works in LangGraph. It provides a simple example that    
# introduces a breakpoint before tools are executed, allowing for human intervention.\n\nThese resources should give you a solid understanding of how LangGraph functions in a human-in-the-loop 
# context.",
#                 additional_kwargs={'refusal': None},
#                 response_metadata={
#                     'token_usage': {
#                         'completion_tokens': 182,
#                         'prompt_tokens': 265,
#                         'total_tokens': 447,
#                         'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                         'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                     },
#                     'model_name': 'gpt-4o-mini-2024-07-18',
#                     'system_fingerprint': 'fp_0705bf87c0',
#                     'finish_reason': 'stop',
#                     'logprobs': None
#                 },
#                 id='run-6943b987-9449-48b4-afd1-e53b2e4e2362-0',
#                 usage_metadata={
#                     'input_tokens': 265,
#                     'output_tokens': 182,
#                     'total_tokens': 447,
#                     'input_token_details': {'audio': 0, 'cache_read': 0},
#                     'output_token_details': {'audio': 0, 'reasoning': 0}
#                 }
#             ),
#             HumanMessage(content="Remember what I'm learning about?", additional_kwargs={}, response_metadata={}, id='33a739db-321f-4248-a98d-11b814738664'),
#             AIMessage(
#                 content="Yes, you're learning about LangGraph, specifically its human-in-the-loop workflow. If you have any specific questions or need further information about LangGraph, feel free toask!",
#                 additional_kwargs={'refusal': None},
#                 response_metadata={
#                     'token_usage': {
#                         'completion_tokens': 36,
#                         'prompt_tokens': 460,
#                         'total_tokens': 496,
#                         'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                         'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                     },
#                     'model_name': 'gpt-4o-mini-2024-07-18',
#                     'system_fingerprint': 'fp_0705bf87c0',
#                     'finish_reason': 'stop',
#                     'logprobs': None
#                 },
#                 id='run-b93ac930-f6cb-4a44-8c9d-f1aa7e9c2a2c-0',
#                 usage_metadata={
#                     'input_tokens': 460,
#                     'output_tokens': 36,
#                     'total_tokens': 496,
#                     'input_token_details': {'audio': 0, 'cache_read': 0},
#                     'output_token_details': {'audio': 0, 'reasoning': 0}
#                 }
#             )
#         ]
#     },
#     next=(),
#     config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1efa8751-941e-6b55-8007-2b06cc228af7'}},
#     metadata={
#         'source': 'loop',
#         'writes': {
#             'chatbot': {
#                 'messages': [
#                     AIMessage(
#                         content="Yes, you're learning about LangGraph, specifically its human-in-the-loop workflow. If you have any specific questions or need further information about LangGraph, feelfree to ask!",
#                         additional_kwargs={'refusal': None},
#                         response_metadata={
#                             'token_usage': {
#                                 'completion_tokens': 36,
#                                 'prompt_tokens': 460,
#                                 'total_tokens': 496,
#                                 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                                 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                             },
#                             'model_name': 'gpt-4o-mini-2024-07-18',
#                             'system_fingerprint': 'fp_0705bf87c0',
#                             'finish_reason': 'stop',
#                             'logprobs': None
#                         },
#                         id='run-b93ac930-f6cb-4a44-8c9d-f1aa7e9c2a2c-0',
#                         usage_metadata={
#                             'input_tokens': 460,
#                             'output_tokens': 36,
#                             'total_tokens': 496,
#                             'input_token_details': {'audio': 0, 'cache_read': 0},
#                             'output_token_details': {'audio': 0, 'reasoning': 0}
#                         }
#                     )
#                 ]
#             }
#         },
#         'thread_id': '2',
#         'step': 7,
#         'parents': {}
#     },
#     created_at='2024-11-22T01:57:16.016520+00:00',
#     parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1efa8751-8bd4-6fd7-8006-c951bc537177'}},
#     tasks=()
# )