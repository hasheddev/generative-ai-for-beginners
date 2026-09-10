from pinecone import ServerlessSpec, Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY"),
    )

#The  metric argument can take the strings 'cosine', 'euclidean', or 'dotproduct'.
if not  pc.has_index("datacamp-index"):
    pc.create_index(
        name="datacamp-index", 
        dimension=1536, 
        spec=ServerlessSpec(
            cloud='aws', 
            region='us-east-1'
        )
    )

def get_datacamp_index():
    index = pc.Index("datacamp-index")
    return index