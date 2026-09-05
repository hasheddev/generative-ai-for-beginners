from openai import OpenAI
from scipy.spatial import distance
import numpy as np

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to obtain embeddings
def create_embeddings(texts):
    response = client.embeddings.create(
        model='text-embedding-3-small',
        input=texts
    )

    response_dict = response.model_dump()
    return [data['embedding'] for data in response_dict['data']]

def calculate_closeness(a, b):
    return distance.cosine(a, b)

def get_min_index(lst):
    return np.argmin(lst)