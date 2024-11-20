import enhancing_chatbot_tools as ect
from rich import print as rprint

result = ect.graph.invoke({"messages": [("user", "What do you know about LangGraph?")]})
rprint(result)
# {
#     'messages': [
#         HumanMessage(content='What do you know about LangGraph?', additional_kwargs={}, response_metadata={}, id='55abdc3c-eb4a-4745-9f65-f6704674ca7c'),
#         AIMessage(
#             content=[
#                 {'text': "To provide you with accurate and up-to-date information about LangGraph, I'll need to search for the latest details. Let me do that for you.", 'type': 'text'},
#                 {'id': 'toolu_01THLCTthSTEiZEj9DoieBM8', 'input': {'query': 'LangGraph AI framework'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}
#             ],
#             additional_kwargs={},
#             response_metadata={
#                 'id': 'msg_015UYh5YwLZfqJ6mK6utZAwX',
#                 'model': 'claude-3-5-sonnet-20240620',
#                 'stop_reason': 'tool_use',
#                 'stop_sequence': None,
#                 'usage': {'input_tokens': 406, 'output_tokens': 97}
#             },
#             id='run-ed8b141c-a684-4587-9d0c-6c2df37fce43-0',
#             tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'LangGraph AI framework'}, 'id': 'toolu_01THLCTthSTEiZEj9DoieBM8', 'type': 'tool_call'}],
#             usage_metadata={'input_tokens': 406, 'output_tokens': 97, 'total_tokens': 503, 'input_token_details': {}}
#         ),
#         ToolMessage(
#             content='[{"url": "https://www.langchain.com/langgraph", "content": "LangGraph\'s flexible framework supports diverse control flows - single agent, multi-agent, hierarchical, sequential - 
# and robustly handles realistic, complex scenarios. ... \\"LangGraph has been instrumental for our AI development. Its robust framework for building stateful, multi-actor applications with LLMs has    
# transformed how we evaluate"}, {"url": "https://medium.com/@lucas.dahan/hands-on-langgraph-building-a-multi-agent-assistant-06aa68ed942f", "content": "Recognizing the need to treat AI as a component  
# of a product meant to deliver value is the first step towards a positive ROI. May 29. ... (Agent Framework — LangGraph) Jul 16. Pankaj."}]',
#             name='tavily_search_results_json',
#             id='4259e300-8925-4be0-842e-603dceab2862',
#             tool_call_id='toolu_01THLCTthSTEiZEj9DoieBM8',
#             artifact={
#                 'query': 'LangGraph AI framework',
#                 'follow_up_questions': None,
#                 'answer': None,
#                 'images': [],
#                 'results': [
#                     {
#                         'title': 'LangGraph - LangChain',
#                         'url': 'https://www.langchain.com/langgraph',
#                         'content': 'LangGraph\'s flexible framework supports diverse control flows - single agent, multi-agent, hierarchical, sequential - and robustly handles realistic, complex      
# scenarios. ... "LangGraph has been instrumental for our AI development. Its robust framework for building stateful, multi-actor applications with LLMs has transformed how we evaluate',
#                         'score': 0.99961853,
#                         'raw_content': None
#                     },
#                     {
#                         'title': 'Hands on LangGraph — Building a multi agent assistant',
#                         'url': 'https://medium.com/@lucas.dahan/hands-on-langgraph-building-a-multi-agent-assistant-06aa68ed942f',
#                         'content': 'Recognizing the need to treat AI as a component of a product meant to deliver value is the first step towards a positive ROI. May 29. ... (Agent Framework —        
# LangGraph) Jul 16. Pankaj.',
#                         'score': 0.9995234,
#                         'raw_content': None
#                     }
#                 ],
#                 'response_time': 2.04
#             }
#         ),
#         AIMessage(
#             content='Based on the search results, I can provide you with information about LangGraph:\n\nLangGraph is an AI framework designed for building advanced language model applications. Here  
# are the key points:\n\n1. Flexible Framework: LangGraph offers a flexible framework that supports various control flows, including:\n   - Single agent\n   - Multi-agent\n   - Hierarchical\n   -       
# Sequential\n\n2. Complex Scenario Handling: It\'s designed to robustly handle realistic and complex scenarios in AI applications.\n\n3. Stateful Applications: LangGraph provides a framework for       
# building stateful applications with Large Language Models (LLMs). This means it can maintain context and state across interactions, which is crucial for more sophisticated AI systems.\n\n4. 
# Multi-Actor Support: The framework is particularly noted for its ability to handle multi-actor applications, suggesting it\'s well-suited for systems where multiple AI agents need to interact or      
# collaborate.\n\n5. AI Development Tool: It has been described as "instrumental for AI development," indicating its significance in the field of artificial intelligence and language model 
# applications.\n\n6. Part of LangChain: LangGraph appears to be associated with LangChain, a popular framework for developing applications with language models.\n\n7. Evaluation Capabilities: It has   
# reportedly transformed how some developers evaluate their AI applications, suggesting it might offer robust testing or performance assessment features.\n\n8. Used in Product Development: There\'s an  
# emphasis on using LangGraph to treat AI as a component of a product meant to deliver value, which aligns with the goal of achieving a positive return on investment (ROI) in AI projects.\n\nWhile      
# LangGraph seems to be a powerful tool for AI developers, especially those working with complex, multi-agent systems or applications requiring stateful interactions, it\'s worth noting that this       
# information is based on relatively recent sources. The field of AI is rapidly evolving, so there may be even more recent developments or features that aren\'t captured in these search results.',      
#             additional_kwargs={},
#             response_metadata={
#                 'id': 'msg_01N9gRzk26HXYDMccRLmRX5z',
#                 'model': 'claude-3-5-sonnet-20240620',
#                 'stop_reason': 'end_turn',
#                 'stop_sequence': None,
#                 'usage': {'input_tokens': 700, 'output_tokens': 422}
#             },
#             id='run-3761d1ff-fc18-4b10-bd43-8cbcb2053a22-0',
#             usage_metadata={'input_tokens': 700, 'output_tokens': 422, 'total_tokens': 1122, 'input_token_details': {}}
#         )
#     ]
# }

            