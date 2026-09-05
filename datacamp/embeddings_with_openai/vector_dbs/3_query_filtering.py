import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient(
    path='./db'
)

collection = client.get_collection(
        name=''netflix_titles'',
        embedding_function=OpenAIEmbeddingFunction(
                model_name="text-embedding-3-small",
                api_key="<OPENAI_API_TOKEN>"
        )
    )

reference_ids = ['s999', 's1000']

reference_texts = collection.get(ids=reference_ids)['documents']

# Query using reference_texts
result = collection.query(
   query_texts=reference_texts,
  n_results=3
)

print(result['documents'])

reference_texts = ["children's story about a car", "lions"]

# Query two results using reference_texts
result = collection.query(
  query_texts=reference_texts,
  n_results=2,
  # Filter for titles with a G rating released before 2019
  where={
    "$and": [
        {"rating": 
        	{"$eq": "G"}
        },
        {"release_year": 
         	{"$lt": 2019}
        }
    ]
  }
)

print(result['documents'])

