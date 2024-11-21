### MemorySaver: An in-memory checkpoint saver. (앞서 살짝 언급한 Checkpointer의 한 종류로 보임)
# This checkpoint saver stores checkpoints in memory using a defaultdict.
# Only use MemorySaver for debugging or testing purposes. 
# For production use cases we recommend installing langgraph-checkpoint-postgres and using PostgresSaver / AsyncPostgresSaver.
# <https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver>

import asyncio

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph
from rich import print as rprint


builder = StateGraph(int)
builder.add_node("add_one", lambda x: x + 1)
builder.set_entry_point("add_one")
builder.set_finish_point("add_one")

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

# coro = graph.ainvoke(1, {"configurable": {"thread_id": "thread-1"}})
# asyncio.run(coro)  # Output: 2
async def main():
    result = await graph.ainvoke(1, {"configurable": {"thread_id": "thread-1"}})
    print(result)  # 결과 출력


##################################################################################
### 1. run main
print('1.', '*'*50)
##################################################################################
asyncio.run(main())

snapshot = graph.get_state({"configurable": {"thread_id": "thread-1"}})
rprint(snapshot) 
# 1. **************************************************
# 2
# StateSnapshot(
#     values=2,
#     next=(),
#     config={'configurable': {'thread_id': 'thread-1', 'checkpoint_ns': '', 'checkpoint_id': '1efa7c0f-ff55-6900-8001-e7a1ff8c86af'}},
#     metadata={'source': 'loop', 'writes': {'add_one': 2}, 'thread_id': 'thread-1', 'step': 1, 'parents': {}},
#     created_at='2024-11-21T04:28:04.160332+00:00',
#     parent_config={'configurable': {'thread_id': 'thread-1', 'checkpoint_ns': '', 'checkpoint_id': '1efa7c0f-ff53-61eb-8000-e3c6f5c82a4d'}},
#     tasks=()
# )
