import add_memory_chatbot as amc

##################################################################################
### 1. thread_id: 1 -> 이름을 말하면서 인사
print('1.', '*'*50)
##################################################################################   
config = {"configurable": {"thread_id": "1"}}

user_input = "Hi there! My name is Will."

# The config is the **second positional argument** to stream() or invoke()!
events = amc.graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)
for event in events:
    event["messages"][-1].pretty_print()
# 1. **************************************************
# ================================ Human Message =================================

# Hi there! My name is Will.
# ================================== Ai Message ==================================

# Hi Will! How can I assist you today?    
    
    
##################################################################################
### 2. thread_id: 1 -> 내 이름을 기억하는지 물어보기
print('2.', '*'*50)
##################################################################################
user_input = "Remember my name?"

# The config is the **second positional argument** to stream() or invoke()!
events = amc.graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="values"
)
for event in events:
    event["messages"][-1].pretty_print()
# 2. **************************************************
# ================================ Human Message =================================

# Remember my name?
# ================================== Ai Message ==================================

# Yes, I remember your name is Will! How can I help you today?

    
##################################################################################
### 3. thread_id: 2 -> thread_id 변경 -> 내 이름을 기억하는지 물어보기
print('3.', '*'*50)
##################################################################################
user_input = "Remember my name?"

# The only difference is we change the `thread_id` here to "2" instead of "1"
events = amc.graph.stream(
    {"messages": [("user", user_input)]},
    {"configurable": {"thread_id": "2"}},
    stream_mode="values",
)
for event in events:
    event["messages"][-1].pretty_print()
# 3. **************************************************
# ================================ Human Message =================================

# Remember my name?
# ================================== Ai Message ==================================

# I don't have the ability to remember past interactions or personal information. However, I'm here to help you with any questions or topics you'd like to discuss! What can I assist you with today? 