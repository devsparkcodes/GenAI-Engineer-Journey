from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.6
)

template = PromptTemplate(
    template="Explain {topic} like a beginner.",
    input_variables=["topic"]
)

final_prompt = template.format(
    topic="Python"
)

response = llm.invoke(final_prompt)

print(response.content)