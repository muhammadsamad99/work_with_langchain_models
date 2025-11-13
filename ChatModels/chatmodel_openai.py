from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatmodel_openai = ChatOpenAI(model="gpt-4", temperature=0.5, max_completion_tokens=10)
chatmodel_openai.invoke("Write 10 lines on AI")
print(chatmodel_openai.content)
