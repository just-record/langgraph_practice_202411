# Lang graph - Tutorials - Quick Start

## Part3: Adding Memory to the Chatbot

<https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-3-adding-memory-to-the-chatbot>

- `add_memory_chatbot.py`: 공식문서의 전체 소스 코드
- `add_memory_chatbot_nomemory.py`: 공식문서의 전체 소스 코드에서 checkpointer인 MemorySaver()를 제외한 버전

- `01.amc_invoke.py`: 공식문서의 전체 소스 코드의 graph를 invoke하여 결과 보기 - 대화 기억 테스트 포함
- `02.amc_langsmith_trace.py`: LangSmith의 trace를 사용해 보기
- `03.amc_checkpoint.py`: 'get_state()'로 checkpoint를 보기
- `04.amc_memorysaver_v1.py`: 전체 소스 코드에서 'MemorySaver()'를 설정하지 않고 사용해 보기
- `05.amc_memorysaver_v2.py`: 'MemorySaver()'예제 소스 코드 사용해 보기
