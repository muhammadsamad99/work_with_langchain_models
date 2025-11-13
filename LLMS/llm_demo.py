from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_llm = OpenAI(model="gpt-3.5-turbo-instruct")
response = openai_llm.invoke("What is capital of Lahore")
print(response)
