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

result = collection.query(query_texts=[], n_results=3)

collection.update(ids=[], documents=[])#upsert
#client.reset()

result = collection.query(query_texts=["films about dogs"], n_results=3)

print(result)

new_data = [
    {"id": "s1001", "document": "Title: Cats & Dogs (Movie)\nDescription: A look at the top-secret, high-tech espionage war going on between cats and dogs, of which their human owners are blissfully unaware."},
    {"id": "s6884", "document": 'Title: Goosebumps 2: Haunted Halloween (Movie)\nDescription: Three teens spend their Halloween trying to stop a magical book, which brings characters from the "Goosebumps" novels to life.\nCategories: Children & Family Movies, Comedies'}
 ]


extracted_ids = [data['id'] for data in new_data]
documents = [data['document'] for data in new_data]
# Update or add the new documents
collection.upsert(
    ids=extracted_ids,
    documents=documents
)

# Delete the item with ID "s95"
collection.delete(ids=['s95'])

result = collection.query(
    query_texts=["films about dogs"],
    n_results=3
)
print(result)