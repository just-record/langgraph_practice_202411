# Tutorials - Use cases - Chatbots

## Build a Customer Support Bot

<https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/>

- `00.prerequisites.py`: 필요 패키지 설치, 환경 변수 설정, DB 다운로드, 최초 1회 실행, DB update 하고자 할 때 실행
- `support_bot_tools.py`: 도구 모음
- `utilities.py`: 유틸리티 모음

✔️ **Part1 Zero-shot agent**

- `p1_zero_shot_agent.py`: Part1 Zero-shot agent
- `01.p1_example_conversation.py`: Part1 Zero-shot agent 샘플 대화
  - 공식문서의 결과 보기: <https://smith.langchain.com/public/f9e77b80-80ec-4837-98a8-254415cb49a1/r/26146720-d3f9-44b6-9bb9-9158cde61f9d>

![part1 - graph](part_1_graph.png)

✔️ **Part2 Add Confirmation**

- `p2_add_confirmation.py`: Part2 Add Confirmation
- `02.p2_example_conversation.py`: Part2 Add Confirmation 샘플 대화
  - 공식문서의 결과 보기: <https://smith.langchain.com/public/b3c71814-c366-476d-be6a-f6f3056caaec/r>

![part2 - graph](part_2_graph.png)

✔️ **Part3 Conditional Interrupt**

- `p3_conditional_interrupt.py`: Part3 Conditional Interrupt
- `03.p3_example_conversation.py`: Part3 Conditional Interrupt 샘플 대화
  - 공식문서의 결과 보기: <https://smith.langchain.com/public/a0d64d8b-1714-4cfe-a239-e170ca45e81a/r>

![part3 - graph](part_3_graph.png)

✔️ **Part4 Specialized Workflows**

결과가 좋지 않은 듯. 시간을 두고 분석 필요

- `p4_specialized_workflow.py`: Part4 Specialized Workflows
- `04.p4_specialized_workflow.py`: Part4 Specialized Workflows 샘플 대화

![part4 - graph](part_4_graph.png)
