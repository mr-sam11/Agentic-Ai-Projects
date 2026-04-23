




from langgraph.graph import START,END,StateGraph
from src.langgraph.llm.groqllm import GroqLLM
from src.langgraph.state.chatbotstate import State
from langchain.messages import HumanMessage
from pydantic import BaseModel
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from src.langgraph.nodes.chatbotnode import ChatBotNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(State)

    def Basic_chatbot_build_graph(self):
      
        chat_bot=ChatBotNode(self.llm)
        self.graph.add_node("chatbot",chat_bot.chatbot)
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)    

        return self.graph    