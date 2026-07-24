from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

response = llm.invoke("What is Artificial Intelligence?")

print(type(response))
print(response.content)
print(response.id)
print(response.response_metadata)
print(response.usage_metadata)