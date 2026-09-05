import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import tiktoken

client = chromadb.PersistentClient(
    path='./db'
)

collection = client.create_collection(
    name='netflix_titles',
    embedding_function=OpenAIEmbeddingFunction(
            model_name="text-embedding-3-small",
            api_key="<OPENAI_API_TOKEN>"
        )
    )

client.list_collections()

documents = []

enc = tiktoken.encoding_for_model("text-embedding-3-small")

# Encode each text in documents and calculate the total tokens
total_tokens = sum(len(enc.encode(document)) for document in documents)

cost_per_1k_tokens = 0.00002

# Display number of tokens and cost
print('Total tokens:', total_tokens)
print('Cost:', total_tokens * cost_per_1k_tokens / 1000)

ids = []

collection.add(ids=ids, documents=documents)

print(f"No. of documents: {collection.count()}")
print(f"First ten documents: {collection.peek()}")