import build_basic_chatbot as bbc
from rich import print as rprint

##################################################################################
### 1. 공식문서의 chat loop 예시
print('1.', '*'*50)
##################################################################################
def stream_graph_updates(user_input: str):
    for event in bbc.graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


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

# 1. **************************************************
# User: hi
# Assistant: Hello! How can I assist you today?
# User: My name is Jildong Hong
# Assistant: Hello, Jildong Hong! How can I assist you today?
# User: What's my name?
# Assistant: I don't know your name. If you'd like to share it, feel free!
# User: q
# Goodbye!

### [[대화를 기억하지 못하는 것 같음]] ###
    