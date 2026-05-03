from langgraph.graph import StateGraph,START,END
from typing import Literal,TypedDict,Annotated
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
import os

load_dotenv()



class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

llm=ChatGroq(model="llama-3.3-70b-versatile")
  #llm.invoke("How the hell are you")

def chat_node(state:ChatState):
    
    #user query
    messages=state['messages']

    #send to llm
    response= llm.invoke(messages)
    
    #return response to state

    return {'messages':[response]}

checkpointer=MemorySaver()

#define graph
graph=StateGraph(ChatState)

# define nodes

graph.add_node('chat_node',chat_node)

#defining edges

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)


CONFIG= {'configurable':{'thread_id':'thread-1'}}

# response=chatbot.invoke({'messages':[HumanMessage(content='Say my name')]}, config=CONFIG)
# print("AI: ",response['messages'][-1].content)
    

# CONFIG= {'configurable':{'thread_id':'1'}}

# for message_chunk,metadata in chatbot.stream(
#     {'messages':[HumanMessage(content="Tell me about BMW")]},
#     config=CONFIG,
#     stream_mode='messages'):
#     if message_chunk.content:
#         print(message_chunk.content,end=" ",flush=True)

# initial_state = {
#     'messages':[HumanMessage(content="Fifa")]
#     }

#chatbot.invoke(initial_state)['messages'][-1].content
# thread_id='1'

# while True:
#     user_input=input("Enter your query:")

#     print("User: ",user_input)

#     if user_input.strip().lower() in ['exit','bye']:
#         break

#     config= {'configurable':{'thread_id':thread_id}} 

#     response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]}, config=config)
#     print("AI: ",response['messages'][-1].content)
    
