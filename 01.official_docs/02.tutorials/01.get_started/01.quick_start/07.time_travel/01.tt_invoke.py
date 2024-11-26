import time_travel as tt
from rich import print as rprint

##################################################################################
### 1. graph invoke - 'tavily_search_results_json' tool 호출 - "human" node를 호출 하지 않음
print('1.', '*'*50)
##################################################################################
config = {"configurable": {"thread_id": "1"}}
events = tt.graph.stream(
    {
        "messages": [
            ("user", "I'm learning LangGraph. Could you do some research on it for me?")
        ]
    },
    config,
    stream_mode="values",
)
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 1. **************************************************
# ================================ Human Message =================================

# I'm learning LangGraph. Could you do some research on it for me?
# response.tool_calls: [{'name': 'tavily_search_results_json', 'args': {'query': 'LangGraph'}, 'id': 'call_igF1KDlmpW4x2BegUhQdJRdQ', 'type': 'tool_call'}]
# ================================== Ai Message ==================================
# Tool Calls:
#   tavily_search_results_json (call_igF1KDlmpW4x2BegUhQdJRdQ)
#  Call ID: call_igF1KDlmpW4x2BegUhQdJRdQ
#   Args:
#     query: LangGraph
# ================================= Tool Message =================================
# Name: tavily_search_results_json

# [{"url": "https://www.datacamp.com/tutorial/langgraph-tutorial", "content": "LangGraph is a library within the LangChain ecosystem that simplifies the development of complex, multi-agent large language model (LLM) applications. Learn how to use LangGraph to create stateful, flexible, and scalable systems with nodes, edges, and state management."}, {"url": "https://langchain-ai.github.io/langgraph/", "content": "LangGraph is a low-level framework that allows you to create stateful, multi-actor applications with LLMs, using cycles, controllability, and persistence. Learn how to use LangGraph with LangChain, LangSmith, and Anthropic tools to build agent and multi-agent workflows."}]
# response.tool_calls: []
# ================================== Ai Message ==================================

# Here are some key resources and information about LangGraph:

# 1. **Overview of LangGraph**:
#    - LangGraph is a library within the LangChain ecosystem designed to simplify the development of complex, multi-agent large language model (LLM) applications.
#    - It allows for the creation of stateful, flexible, and scalable systems by utilizing nodes, edges, and state management.

#    You can read more about it [here](https://www.datacamp.com/tutorial/langgraph-tutorial).

# 2. **Framework Features**:
#    - LangGraph serves as a low-level framework that enables the creation of stateful, multi-actor applications using LLMs.
#    - It supports cycles, controllability, and persistence, making it suitable for building complex workflows.

#    For detailed documentation, you can visit the official site [here](https://langchain-ai.github.io/langgraph/).

# These resources should help you get started with LangGraph and understand its functionalities better. If you have specific questions or need further information, feel free to ask!        


##################################################################################
### 2. 추가 요청 - 'tavily_search_results_json' tool 호출 - "human" node를 호출 하지 않음
print('2.', '*'*50)
##################################################################################
events = tt.graph.stream(
    {
        "messages": [
            # ("user", "Ya that's helpful. Maybe I'll build an autonomous agent with it!")
            ("user", "Ya that's helpful. Maybe I'll build an autonomous agent with it!. Please search for information on how to get started.")
        ]
    },
    config,
    stream_mode="values",
)
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 2. **************************************************
# ================================ Human Message =================================

# Ya that's helpful. Maybe I'll build an autonomous agent with it!
# response.tool_calls: []
# ================================== Ai Message ==================================

# That sounds like an exciting project! Building an autonomous agent with LangGraph can open up many possibilities for creating intelligent systems that can interact, learn, and adapt. If you have any specific ideas in 
# mind or need assistance with certain aspects of your project, feel free to ask. Good luck with your development!     

### [[ 공식 예제 처럼 tool call(tavily_search_results_json)을 호출 하지 않네 ]]
### [[ test를 위해 Anthropic 모델로 변경 ]]
# 2. **************************************************
# ================================ Human Message =================================

# Ya that's helpful. Maybe I'll build an autonomous agent with it!
# response.tool_calls: []
# ================================== Ai Message ==================================

# That's a great idea! Building an autonomous agent with LangGraph could be an excellent way to learn the framework and explore its capabilities. Here are some suggestions and considerations for your project:

# 1. Start with a simple agent:
#    Begin with a basic autonomous agent that has a clear, focused task. This will help you understand the core concepts of LangGraph without getting overwhelmed.

### [[ Anthropic 모델도 AI가 직접 답변하고 종료 ]]

### [[ Prompt 변경 ]]
### [[ 'Please search for information on how to get started.' 추가 ]] ###
# 2. **************************************************
# ================================ Human Message =================================

# Ya that's helpful. Maybe I'll build an autonomous agent with it!. Please search for information on how to get started.
# response.tool_calls: [{'name': 'tavily_search_results_json', 'args': {'query': 'how to get started with LangGraph'}, 'id': 'call_Po0D3IpTxHJOMmVWEyu8Mqhk', 'type': 'tool_call'}]
# ================================== Ai Message ==================================
# Tool Calls:
#   tavily_search_results_json (call_Po0D3IpTxHJOMmVWEyu8Mqhk)
#  Call ID: call_Po0D3IpTxHJOMmVWEyu8Mqhk
#   Args:
#     query: how to get started with LangGraph
# ================================= Tool Message =================================
# Name: tavily_search_results_json

# [{"url": "https://www.datacamp.com/tutorial/langgraph-tutorial", "content": "Getting Started With LangGraph. Let's see how we can set up LangGraph and what the basic concepts are. Installation. To install LangGraph, you can use pip: pip install -U langgraph Basic Concepts. Nodes: Nodes represent units of work within your LangGraph. They are typically Python functions that perform a specific task, such as:"}, {"url": "https://medium.com/@gopiariv/langgraph-a-beginners-guide-to-building-ai-workflows-e500965f2ef9", "content": "We'll also walk through a simple example to get you started. What is LangGraph? LangGraph is an extension of the popular 
# LangChain library. It allows you to create AI applications that can"}]
# response.tool_calls: []
# ================================== Ai Message ==================================

# Here are some resources that can help you get started with LangGraph:


##################################################################################
### 3. 모든 state 내역 조회 -> 6개의 chat message가 있는 state를 to_replay로 저장
print('3.', '*'*50)
##################################################################################
to_replay = None
for state in tt.graph.get_state_history(config):
    print("Num Messages: ", len(state.values["messages"]), "Next: ", state.next)
    print("-" * 80)
    if len(state.values["messages"]) == 6:
        # We are somewhat arbitrarily selecting a specific state based on the number of chat messages in the state.
        to_replay = state
# 3. **************************************************
# Num Messages:  8 Next:  ()
# --------------------------------------------------------------------------------
# Num Messages:  7 Next:  ('chatbot',)
# --------------------------------------------------------------------------------
# Num Messages:  6 Next:  ('tools',)
# --------------------------------------------------------------------------------
# Num Messages:  5 Next:  ('chatbot',)
# --------------------------------------------------------------------------------
# Num Messages:  4 Next:  ('__start__',)
# --------------------------------------------------------------------------------
# Num Messages:  4 Next:  ()
# --------------------------------------------------------------------------------
# Num Messages:  3 Next:  ('chatbot',)
# --------------------------------------------------------------------------------
# Num Messages:  2 Next:  ('tools',)
# --------------------------------------------------------------------------------
# Num Messages:  1 Next:  ('chatbot',)
# --------------------------------------------------------------------------------
# Num Messages:  0 Next:  ('__start__',)
# --------------------------------------------------------------------------------        


##################################################################################
### 4. to_replay에 저장된 state를 조회
print('4.', '*'*50)
##################################################################################
rprint(to_replay.next)
rprint(to_replay.config)
# 4. **************************************************
# ('tools',)
# {'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1efaba48-02f5-64e8-8006-fd88996449fc'}}



##################################################################################
### 5. to_replay에 저장된 state로 되감기
print('5.', '*'*50)
##################################################################################
# The `checkpoint_id` in the `to_replay.config` corresponds to a state we've persisted to our checkpointer.
for event in tt.graph.stream(None, to_replay.config, stream_mode="values"):
    if "messages" in event:
        event["messages"][-1].pretty_print()
# 5. **************************************************
# ================================== Ai Message ==================================
# Tool Calls:
#   tavily_search_results_json (call_Z4pRUAf0vPn8WaahgL5mRj8C)
#  Call ID: call_Z4pRUAf0vPn8WaahgL5mRj8C
#   Args:
#     query: getting started with LangGraph autonomous agent
# ================================= Tool Message =================================
# Name: tavily_search_results_json

# [{"url": "https://www.langchain.com/langgraph", "content": "With built-in statefulness, LangGraph agents seamlessly collaborate with humans by writing drafts for review and awaiting approval before acting. Easily inspect the agent's actions and \"time-travel\" to roll back and take a different action to correct course. ... Get started with LangChain, LangSmith, and LangGraph to enhance your LLM app"}, {"url": "https://medium.com/coinmonks/a-step-by-step-guide-to-building-ai-agents-with-langgraph-6d21d6e6e34f", "content": "A Step-by-Step Guide to Building AI Agents with LangGraph | by Alannaelga | Coinmonks | Nov, 2024 | Medium LangGraph allows you to define workflows that include various tools and tasks that the AI agent can perform. LangGraph AI agents can function as virtual assistants, providing users with personalized support for various tasks, from scheduling to data management. Task Automation: AI agents can schedule meetings, set reminders, send emails, and even manage to-do lists, all while learning user preferences and optimizing workflows over time."}]       
# response.tool_calls: []
# ================================== Ai Message ==================================

# Here are some resources and steps to get started with building an autonomous agent using LangGraph:

# 1. **Overview of LangGraph Agents**:
#    LangGraph agents are designed to work collaboratively with humans, allowing them to draft actions for review before execution. They feature built-in statefulness, which enables you to inspect the agent's actions and even "time-travel" to revert to previous states if needed.

# 2. **Step-by-Step Guide**:
#    A detailed guide is available on Medium titled ["A Step-by-Step Guide to Building AI Agents with LangGraph"](https://medium.com/coinmonks/a-step-by-step-guide-to-building-ai-agents-with-langgraph-6d21d6e6e34f). This guide outlines how to define workflows that incorporate various tools and tasks for the AI agent, enabling it to function as a virtual assistant. Key features include:
#    - Task automation, such as scheduling meetings, sending reminders, and managing to-do lists.
#    - Learning user preferences over time to optimize workflows.        