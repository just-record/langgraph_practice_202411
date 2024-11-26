from rich import print as rprint
from langgraph.graph.message import add_messages

##################################################################################
### 1. add_messages test: ['hi'], ['hello']
print('1.', '*'*50)
##################################################################################
added = add_messages(left=['hi'], right=['hello'])
# added = add_messages(['hi'], ['hello'])

rprint(added)
print('-'*20)
rprint(added[0])
print('-'*20)
rprint(added[0].content)
# 1. **************************************************
# [
#     HumanMessage(content='hi', additional_kwargs={}, response_metadata={}, id='c39735f3-1935-4517-b949-187593c26f9f'),
#     HumanMessage(content='hello', additional_kwargs={}, response_metadata={}, id='1e0db0cf-8e58-4006-bd5d-b4e03f3550fd')
# ]
# --------------------
# HumanMessage(content='hi', additional_kwargs={}, response_metadata={}, id='c39735f3-1935-4517-b949-187593c26f9f')
# --------------------
# hi


### [[add_messages의 작동법]] ###
### 입력된 list의 요소를 HumanMessage로 변환하고 left와 right를 합친다. ###

##################################################################################
### 2. add_messages test: added, added
print('2.', '*'*50)
##################################################################################
added_2 = add_messages(left=added, right=['good', 'morning'])

rprint(added_2)
print('-'*20)
rprint(added_2[-1])
print('-'*20)
rprint(added_2[-1].content)
# 2. **************************************************
# [
#     HumanMessage(content='hi', additional_kwargs={}, response_metadata={}, id='c39735f3-1935-4517-b949-187593c26f9f'),
#     HumanMessage(content='hello', additional_kwargs={}, response_metadata={}, id='1e0db0cf-8e58-4006-bd5d-b4e03f3550fd'),
#     HumanMessage(content='good', additional_kwargs={}, response_metadata={}, id='9e8e9dd3-b3a0-41bf-b157-be65ad971ad5'),
#     HumanMessage(content='morning', additional_kwargs={}, response_metadata={}, id='c6ae0db1-76f5-4380-950f-5f7eee112d36')
# ]
# --------------------
# HumanMessage(content='morning', additional_kwargs={}, response_metadata={}, id='c6ae0db1-76f5-4380-950f-5f7eee112d36')
# --------------------
# morning
