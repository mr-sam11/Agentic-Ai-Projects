from src.langgraph.llm.groqllm import GroqLLM
from langchain.messages import HumanMessage
from src.langgraph.graph.graph_builder import GraphBuilder
import streamlit as st



def load_langgraph_agenticai_app():
    groqllm=GroqLLM()
    llm=groqllm.get_llm()

    #Building a graph
    graph=GraphBuilder(llm)

    workflow_graph=graph.Basic_chatbot_build_graph()
    workflow=workflow_graph.compile()
    # inital_state={"messages":[HumanMessage(content="Kitty")]}
    # response=workflow.invoke(inital_state)


    user_input=st.chat_input("enter the query")

            
    if user_input:
            
        #st.session_state['message_history'].append({'role':'user','content':user_input})

                with st.chat_message('user'):
                    st.text(user_input)
                
                #Ai_response=workflow.stream({'messages':[HumanMessage(content=user_input)]},stream_mode='messages')
            
                #st.session_state['message_history'].append({'role':'assistant','content':Ai_response['messages'][-1].content})
                with st.chat_message('assistant'):
                    #st.text(Ai_response['messages'][-1].content)
                    st.write_stream(
                                chunk.content for chunk, metadata in workflow.stream(
                                {'messages':[HumanMessage(content=user_input)]},
                                stream_mode='messages'
                                )
                            )
    # graph=StateGraph(State

    # chat_bot=ChatBotNode(llm)

    # graph.add_node("chatbot",chat_bot.chatbot)
    # graph.add_edge(START,"chatbot")
    # graph.add_edge("chatbot",END)