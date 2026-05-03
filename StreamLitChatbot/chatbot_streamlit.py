import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG= {'configurable':{'thread_id':'1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

for messages in st.session_state['message_history']:
    with st.chat_message(messages['role']):
        st.text(messages['content'])


user_input=st.chat_input("enter the query")

if user_input:
    
    st.session_state['message_history'].append({'role':'user','content':user_input})

    with st.chat_message('user'):
        st.text(user_input)
    
    Ai_response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]}, config=CONFIG)

    st.session_state['message_history'].append({'role':'assistant','content':Ai_response['messages'][-1].content})
    with st.chat_message('assistant'):
        st.text(Ai_response['messages'][-1].content)