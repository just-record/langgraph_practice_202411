import build_basic_chatbot as bbc
from rich import print as rprint

##################################################################################
### 1. graph를 stream 하기
print('1.', '*'*50)
##################################################################################
result = bbc.graph.stream({"messages": [{"role": "user", "content": "What do you know about LangGraph?"}]})
rprint(result)

# <generator object Pregel.stream at 0x00000206CB784740>

### [[generator가 return 됨]] ###


##################################################################################
### 2. graph를 stream 하기
### generator를 for loop로 돌리기
print('2.', '*'*50)
##################################################################################
events = bbc.graph.stream({"messages": [{"role": "user", "content": "What do you know about LangGraph?"}]})
for event in events:
    print('-'* 20)
    rprint(event)

# --------------------
# {
#     'chatbot': {
#         'messages': [
#             AIMessage(
#                 content="As of my last update in October 2023, LangGraph is a framework designed to facilitate the development of applications that utilize large language models (LLMs) alongside graph-based data      
# structures. It aims to bridge the gap between natural language processing and knowledge representation by allowing developers to effectively integrate LLMs with graph databases or knowledge graphs.\n\nKey features of 
# LangGraph may include:\n\n1. **Integration of LLMs and Graphs**: LangGraph allows for the seamless combination of language models with graph data, enabling applications that can understand and manipulate complex      
# relationships within data.\n\n2. **Querying and Reasoning**: It provides tools for querying graph data using natural language, making it easier for users to interact with complex datasets without needing extensive    
# programming knowledge.\n\n3. **Use Cases**: LangGraph can be employed in various applications, including chatbots, recommendation systems, and knowledge management tools, where understanding relationships and context 
# is crucial.\n\n4. **Extensibility**: The framework is likely designed to be extensible, allowing developers to customize and build upon its capabilities for specific applications or industries.\n\nFor the latest      
# information, features, and updates about LangGraph, I recommend checking the official documentation or the project's website, as there may have been developments or changes after my last update.",
#                 additional_kwargs={'refusal': None},
#                 response_metadata={
#                     'token_usage': {
#                         'completion_tokens': 257,
#                         'prompt_tokens': 15,
#                         'total_tokens': 272,
#                         'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
#                         'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}
#                     },
#                     'model_name': 'gpt-4o-mini-2024-07-18',
#                     'system_fingerprint': 'fp_0705bf87c0',
#                     'finish_reason': 'stop',
#                     'logprobs': None
#                 },
#                 id='run-38938fce-829c-46ec-a72f-6380b07a0a6c-0',
#                 usage_metadata={'input_tokens': 15, 'output_tokens': 257, 'total_tokens': 272, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
#             )
#         ]
#     }
# }

### [[invoke와 다르게 'chatbot'을 key로 가지는 dictionary가 return 됨 - node 이름]] ###

##################################################################################
### 3. graph를 stream 하기
### event.values()
print('3.', '*'*50)
##################################################################################
events = bbc.graph.stream({"messages": [{"role": "user", "content": "What do you know about LangGraph? Give me two answers."}]})
for event in events:
    for value in event.values():
        print('+'*20)
        for message in value["messages"]:
            # rprint(message)
            rprint(message.content[:100])
        # rprint("Assistant:", value["messages"][-1].content[:100])
# ++++++++++++++++++++
# LangGraph is a framework designed for building applications that integrate natural language processi      


### [[invoke와 stream의 상세한 차이는 아직 잘 모르겠음]] ###


### 인공지능에 문의 결과 ###

# LangGraph의 `invoke`와 `stream` 메서드는 그래프 실행 방식과 결과 반환 방법에서 주요한 차이가 있습니다. 각 메서드의 특징과 차이점을 살펴보겠습니다:

# ## invoke 메서드
# 1. **동기적 실행**: `invoke`는 그래프를 동기적으로 실행합니다. 즉, 그래프의 모든 노드가 순차적으로 실행되고 최종 결과가 반환될 때까지 기다립니다[1].
# 2. **단일 결과 반환**: 그래프 실행이 완료된 후 최종 결과만을 반환합니다[1].
# 3. **간단한 사용**: 단순한 요청이나 빠른 응답이 필요한 경우에 적합합니다[1].
# 4. **메모리 효율**: 전체 실행 결과를 한 번에 메모리에 저장하므로, 대규모 출력의 경우 메모리 사용량이 높을 수 있습니다.

# ## stream 메서드
# 1. **스트리밍 실행**: `stream`은 그래프 실행 중 중간 결과를 실시간으로 스트리밍합니다[5].
# 2. **단계별 결과 반환**: 각 노드의 실행 결과를 순차적으로 반환합니다. 이를 통해 그래프 실행의 진행 상황을 실시간으로 확인할 수 있습니다[5][6].
# 3. **유연한 모드 선택**: 
#    - `values` 모드: 각 단계의 현재 상태 값을 출력합니다[6].
#    - `updates` 모드: 각 단계의 상태 업데이트만 출력합니다(기본값)[6].
#    - `messages` 모드: 각 단계의 메시지를 출력합니다[6].
# 4. **실시간 처리**: 대용량 데이터나 장시간 실행되는 그래프에 적합합니다. 사용자에게 중간 결과를 빠르게 제공할 수 있습니다[5].
# 5. **메모리 효율성**: 전체 결과를 메모리에 저장하지 않고 순차적으로 처리하므로, 대규모 출력 처리에 효율적입니다.
# 6. **비동기 지원**: `astream` 메서드를 통해 비동기 스트리밍도 지원합니다[6].

# ## 주요 차이점 요약
# 1. **실행 방식**: `invoke`는 동기적 실행, `stream`은 스트리밍 실행을 제공합니다.
# 2. **결과 반환**: `invoke`는 최종 결과만 반환, `stream`은 중간 결과를 순차적으로 반환합니다.
# 3. **사용 사례**: `invoke`는 간단하고 빠른 요청에, `stream`은 실시간 처리와 대용량 데이터에 적합합니다.
# 4. **메모리 효율성**: `stream`이 대규모 출력 처리에 더 효율적입니다.
# 5. **유연성**: `stream`은 다양한 모드를 통해 더 세밀한 제어와 실시간 모니터링을 제공합니다.

