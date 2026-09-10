from pinecone import ServerlessSpec, Pinecone
import os
from dotenv import load_dotenv
import itertools

load_dotenv()

pc = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY"),
        pool_threads=30
    )

#The  metric argument can take the strings 'cosine', 'euclidean', or 'dotproduct'.
if not pc.has_index("datacamp-index"):
    pc.create_index(
        name="datacamp-index", 
        dimension=1536, 
        spec=ServerlessSpec(
            cloud='aws', 
            region='us-east-1'
        )
    )

if not pc.has_index("semantic-search-datacamp"):
    pc.create_index(
        name="datacamp-index", 
        dimension=1536, 
        spec=ServerlessSpec(
            cloud='aws', 
            region='us-east-1'
        )
    )

def get_datacamp_index(multi_thread=False):
    index = pc.Index("datacamp-index", pool_threads=30) if multi_thread else pc.Index("datacamp-index")
    return index

def get_search_index(multi_thread=False):
    index = pc.Index("semantic-search-datacamp", pool_threads=30) if multi_thread else pc.Index("semantic-search-datacamp")
    return index

def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))