from src.langgraph.llm.groqllm import GroqLLM
from src.langgraph.state.chatbotstate import State
from src.langgraph.llm.groqllm import GroqLLM
# groqllm=GroqLLM()
# llm=groqllm.get_llm()

class ChatBotNode:
    def __init__(self,llm):
        self.groqllm=llm
    
    def chatbot(self,state:State):
       messages=state.messages
    #    groqllm=GroqLLM()
    #    llm=groqllm.get_llm()   
       #print(llm.invoke(messages).content)
       response=self.groqllm.invoke(messages).content
       print(response)
       return {"messages":[response]}