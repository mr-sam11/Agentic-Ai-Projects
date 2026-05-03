from langgraph.graph import StateGraph,START,END
from typing import Literal,TypedDict,Annotated
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage
# from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
import os

load_dotenv()


os.environ["GROQ_API_KEY"]=apikey=os.getenv("GROQ_API_KEY")


class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

llm=ChatGroq(model="lama-3.3-70b-versatile",api_key=apikey)
  #llm.invoke("How the hell are you")

def chat_node(state:ChatState):
    
    #user query
    messages=state['messages']

    #send to llm
    response= llm.invoke(messages)
    
    #return response to state

    return {'messages':[response]}


conn=sqlite3.connect(database='chatbot.db',check_same_thread=False)

checkpointer=SqliteSaver(conn=conn)

#define graph
graph=StateGraph(ChatState)

# define nodes

graph.add_node('chat_node',chat_node)

#defining edges

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)

def retrive_all_threads():
    all_thread=set()
    for checkpoint in checkpointer.list(None):
      all_thread.add(checkpoint.config['configurable']['thread_id'])

    return list(all_thread)