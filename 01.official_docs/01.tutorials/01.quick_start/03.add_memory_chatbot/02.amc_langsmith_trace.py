### .env file에 Lang Smith API Key를 저장해야 합니다.

# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
# LANGCHAIN_API_KEY=발급받은_API_키
# LANGCHAIN_PROJECT=프로젝트_이름

from dotenv import load_dotenv
load_dotenv()

### 아래 소스 코드는 이전과 동일 ###

import add_memory_chatbot as amc

config = {"configurable": {"thread_id": "1"}}

user_input = "Hi there! My name is Will."

### 1. thread_id: 1 -> 이름을 말하면서 인사
events = amc.graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)
for event in events:
    event["messages"][-1].pretty_print()

### 2. thread_id: 1 -> 내 이름을 기억하는지 물어보기
user_input = "Remember my name?"

events = amc.graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)
for event in events:
    event["messages"][-1].pretty_print()


### 3. thread_id: 2 -> thread_id 변경 -> 내 이름을 기억하는지 물어보기
user_input = "Remember my name?"

# The only difference is we change the `thread_id` here to "2" instead of "1"
events = amc.graph.stream(
    {"messages": [("user", user_input)]},
    {"configurable": {"thread_id": "2"}},
    stream_mode="values",
)
for event in events:
    event["messages"][-1].pretty_print()
    
    
    
### [[Lang Smith 조회하기]] ###   
# 아래의 경로는 Lang Graph에서 제공하는 주소로 보입니다.
# <https://smith.langchain.com/public/29ba22b5-6d40-4fbe-8d27-b369e3329c84/r/6453d5dc-514b-4cb3-837e-37c109a6c6fb