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

import os

# print(apikey)

llm=ChatGroq(model="llama-3.3-70b-versatile")
print(llm.invoke("Hello"))