import streamlit as st
from langgraph_database_backend import retrive_all_threads,chatbot
from langchain_core.messages import HumanMessage
import uuid

# CONFIG= {'configurable':{'thread_id':'1'}}
#-----------------------------util-functions---------------------------

def generatthread():
    thread_id=uuid.uuid4()
    return thread_id

def reset_chat():

    thread_id=generatthread()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
       st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable':{'thread_id':thread_id}}).values['messages']


#----------------------------session-------------------------------------

if 'message_history' not in st.session_state:
     st.session_state['message_history']=[]

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']= generatthread()


if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads']=retrive_all_threads()

add_thread(st.session_state['thread_id'])

#----------------------------UI----------------------   -------------------
st.sidebar.title('Langgraph Chatbot')
if st.sidebar.button('New Chat'):
    reset_chat()
st.sidebar.text('My conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id']=thread_id
        messages=load_conversation(thread_id)
        #print(messages)
        temp_message=[]

        for msg in messages:
            if isinstance(msg,HumanMessage):
                role='user'
            else :
                role='assistant'
            temp_message.append({'role':role,'content':msg.content})  

        st.session_state['message_history']=temp_message          




for messages in st.session_state['message_history']:
    with st.chat_message(messages['role']):
        st.text(messages['content'])


user_input=st.chat_input("enter the query")

CONFIG= {'configurable':{'thread_id':st.session_state['thread_id']}}

if user_input:
    
    st.session_state['message_history'].append({'role':'user','content':user_input})

    with st.chat_message('user'):
        st.text(user_input)
    
    #Ai_response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]}, config=CONFIG)

    # st.session_state['message_history'].append({'role':'assistant','content':Ai_response['messages'][-1].content})
    with st.chat_message('assistant'):
        Ai_response= st.write_stream( message_chunk.content for message_chunk, metadata in chatbot.stream({'messages':[HumanMessage(content=user_input)]},
                           config=CONFIG,
                           stream_mode='messages')
        )

        st.session_state['message_history'].append({'role':'assistant','content':Ai_response})
 