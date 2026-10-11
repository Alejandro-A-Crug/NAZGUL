from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os

load_dotenv()

llm= ChatOpenAI(
    model="meta-llama/llama-3.3-70b-instruct",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
)

response = llm.invoke("¡Hola! ¿Cual es la historia tras el anillo único?")
print(response.content)