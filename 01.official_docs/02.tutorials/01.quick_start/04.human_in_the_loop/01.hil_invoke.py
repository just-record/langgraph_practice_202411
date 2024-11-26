import human_in_the_loop as hil
from rich import print as rprint

##################################################################################
### 1. 'interrupt_before=["tools"]'를 추가하고 invoke() 호출
print('1.', '*'*50)
##################################################################################
user_input = "I'm learning LangGraph. Could you do some research on it for me?"
config = {"configurable": {"thread_id": "1"}}
# The config is the **second positional argument** to stream() or invoke()!
events = hil.graph.stream(
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
#   tavily_search_results_json (call_24qOl7kFanOg20fsJcUnIK1B)
#  Call ID: call_24qOl7kFanOg20fsJcUnIK1B
#   Args:
#     query: LangGraph   

### [[interrupt_before=["tools"]로 인해 tools node 호출 전에 중단됨]] ###    


##################################################################################
### 2. state 조회
print('2.', '*'*50)
##################################################################################
snapshot = hil.graph.get_state(config)
rprint(snapshot.next)

print()

existing_message = snapshot.values["messages"][-1]
rprint(existing_message.tool_calls)

# rprint(snapshot)
# 2. **************************************************
# ('tools',)

# [{'name': 'tavily_search_results_json', 'args': {'query': 'LangGraph'}, 'id': 'call_qgIbpMhB8DGlme3BK5qmyuLT', 'type': 'tool_call'}]

### [[next=('tools',)로 다음 이동 할 node는 tools로 설정 되어 있음]] ###
### [[tool_calls를 확인 하면 tavily_search_results_json로 설정 되어 있음]] ###


##################################################################################
### 3. None을 전달하여 graph 진행 시키기 - 추가되는 것 없음
print('3.', '*'*50)
##################################################################################
# `None` will append nothing new to the current state, letting it resume as if it had never been interrupted
events = hil.graph.stream(None, config, stream_mode="values")
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 3. **************************************************
# ================================== Ai Message ==================================
# Tool Calls:
#   tavily_search_results_json (call_tNeEXXwbuyvmkgn81564OJgy)
#  Call ID: call_tNeEXXwbuyvmkgn81564OJgy
#   Args:
#     query: LangGraph
# ================================= Tool Message =================================
# Name: tavily_search_results_json

# [{"url": "https://www.langchain.com/langgraph", "content": "LangGraph is a stateful, orchestration framework that brings added control to agent workflows. LangGraph Platform is a service for deploying and scaling LangGraph applications, with an opinionated API for building agent UXs, plus an integrated developer studio."}, {"url": "https://langchain-ai.github.io/langgraph/", "content": "LangGraph 
# is a framework for creating stateful, multi-actor applications with LLMs, using cycles, controllability, and persistence. Learn how to use LangGraph with LangChain, LangSmith, and Anthropic tools to build agent and multi-agent workflows."}]
# ================================== Ai Message ==================================

# Here's what I found about LangGraph:

# 1. **Overview**: LangGraph is a stateful orchestration framework designed to provide enhanced control over agent workflows. It allows developers to create applications that can manage complex interactions between multiple actors and large language models (LLMs).

# 2. **Key Features**:
#    - **Stateful Applications**: LangGraph supports the creation of applications that maintain state across different interactions, making it suitable for more complex and interactive workflows.       
#    - **Multi-Actor Support**: It facilitates building applications that involve multiple agents working together, which is beneficial for collaborative tasks.
#    - **Control and Persistence**: The framework offers features for cycle management, controllability, and data persistence, allowing for more robust application development.

# 3. **Deployment and Development**: The LangGraph Platform provides a service for deploying and scaling applications built with LangGraph. It includes an opinionated API tailored for developing user experiences for agent workflows, along with an integrated developer studio for ease of use.

# 4. **Integration**: LangGraph can be utilized alongside other tools like LangChain and LangSmith, as well as Anthropic tools, to build comprehensive agent and multi-agent workflows.

# For more detailed information, you can check the following resources:
# - [LangGraph Official Page](https://www.langchain.com/langgraph)
# - [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)

# If you have specific aspects of LangGraph you'd like to know more about, feel free to ask!        