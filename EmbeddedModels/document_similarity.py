from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from torch import cosine_similarity, embedding

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)
documents = [
    "Babar Azam is an pakistani cricketer",
    "Misbah ul Haq broke fastest century record in test",
    "Shahid Afridi is a tulla player"
]

query = 'tell me about misbah ul haq'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

print(sorted(list(enumerate(scores)), key=lambda x:x[1])[-1])
