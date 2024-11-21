# add_conditional_edges
# <https://langchain-ai.github.io/langgraph/reference/graphs/?h=add+conditional+edges#langgraph.graph.graph.Graph.add_conditional_edges>

### Conditional Edges
# <https://langchain-ai.github.io/langgraph/concepts/low_level/?h=add+conditional+edges#conditional-edges>


### [START]처음 만나면 [인사] - 'hi'
### 'hi'면 [놀기] - 'playing'
### [놀기]놀고 나서 [인사] 'good bye' -> [END]

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    # messages: Annotated[list, add_messages]
    messages: str


def check_greeting(state: State):
    if state["messages"] == 'hi':
        return "playing"
    return END


def greeting(state: State):
    greeting = state["messages"]
    print(f'greeting: {greeting}')
    # return {"messages": 'hello'}


def playing(state: State):
    print(f'playing~~~')
    return {"messages": 'good bye'}


workflow = StateGraph(State)

# Define the two nodes we will cycle between
workflow.add_node("greeting", greeting)
workflow.add_node("playing", playing)

workflow.add_edge(START, "greeting")
workflow.add_conditional_edges("greeting", check_greeting, ["playing", END])
workflow.add_edge("playing", "greeting")

app = workflow.compile()


mermaid_png = app.get_graph().draw_mermaid_png()
with open('greeting.png', 'wb') as f:
    f.write(mermaid_png)
    
##################################################################################
### 1. hi
print('1.', '*'*50)
##################################################################################    
# for chunk in app.stream(
#     {"messages": 'hi'}, stream_mode="values"
# ):
#     # chunk["messages"][-1].pretty_print()
#     print(chunk["messages"][-1])
print(app.invoke({"messages": 'hi'}))
    
    
##################################################################################
### 2. good bye
print('2.', '*'*50)
##################################################################################    
print(app.invoke({"messages": 'good bye'}))