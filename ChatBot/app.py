from langgraph.graph import START,END,StateGraph
from src.langgraph.llm.groqllm import GroqLLM
from src.langgraph.state.chatbotstate import State
from langchain.messages import HumanMessage
from pydantic import BaseModel
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from src.langgraph.nodes.chatbotnode import ChatBotNode

groqllm=GroqLLM()
llm=groqllm.get_llm()
    
chat_bot=ChatBotNode(llm)

graph=StateGraph(State)

graph.add_node("chatbot",chat_bot.chatbot)
graph.add_edge(START,"chatbot")
graph.add_edge("chatbot",END)

workflow=graph.compile()
inital_state={"messages":[HumanMessage(content="Kitty")]}
response=workflow.invoke(inital_state)
