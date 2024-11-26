### 이전의 전체 소스 코드(MemorySaver 설정 하지 않고)로 테스트 해 보기

### [[checkpointer(MemorySaver)를 설정하지 않으면 graph.get_state(config)에서 오류 발생]]
### [[checkpointer(MemorySaver)를 설정하지 않아서 이전 대화를 기억하지 못함]]

import add_memory_chatbot_nomemory as amc   ## 수정된 전체 소스 코드
from rich import print as rprint


config = {"configurable": {"thread_id": "1"}}

##################################################################################
### 1. config만 설정하고 아무 것도 호출하지 않은 상태
print('1.', '*'*50)
##################################################################################   
# snapshot = amc.graph.get_state(config)
# rprint(snapshot)


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
# snapshot = amc.graph.get_state(config)
# rprint(snapshot)  

# 2. **************************************************
# ================================ Human Message =================================

# Remember my name?
# ================================== Ai Message ==================================

# I don't have access to personal data unless you share it with me in this conversation. If you tell me your name, I can remember it for the duration of our chat!  


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
# snapshot = amc.graph.get_state(config)
# rprint(snapshot)


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
print('3.', '*'*50)
##################################################################################       
# snapshot = amc.graph.get_state({"configurable": {"thread_id": "2"}})
# rprint(snapshot)        
