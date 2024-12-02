# Home

<https://langchain-ai.github.io/langgraph/>

- `home.py`: 샘플 예제 코드

## Installation

```bash
pip install -U langgraph
```

```bash
# llm
pip install langchain-anthropic
pip install langchain-openai
```

## API-Key Setting

`.env` 파일

```python
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
# LangSmith 설정
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=lsv2_
LANGCHAIN_PROJECT=LangGraph_home
```

## 소스 코드

`home.py`: 공식문서의 전체 소스 코드

![diagram](diagram.png)

`01.home_invoke.py`: 공식문서의 전체 소스 코드의 graph를 invoke하여 결과 보기
