from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

class GroqLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        os.getenv(os.getenv("GROQ_API_KEY"))
        os.environ["GROQ_API_KEY"]=self.groq_api_key=os.getenv("GROQ_API_KEY")
        llm=ChatGroq(api_key=self.groq_api_key,model="llama-3.3-70b-versatile")
        return llm