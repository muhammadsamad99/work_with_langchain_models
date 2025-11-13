from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model_anthropic = ChatAnthropic(model='claude-3-5-sonnet-20241022')
model_anthropic.invoke("Hi")
print(model_anthropic.content)
