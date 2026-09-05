from openai import OpenAI
from scipy.spatial import distance

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to obtain embeddings
def create_embeddings(texts):
    response = client.embeddings.create(
        model='text-embedding-3-small',
        input=texts
    )

    response_dict = response.model_dump()
    return [data['embedding'] for data in response_dict['data']]

def find_n_closest(query_vector, embdeddings, n=3):
    distances =[]
    for i, embedding in enumerate(embdeddings):
        dist = distance.cosine(query_vector, embedding)
        distances.append({"distance": dist, "index": i})
    sorted_dist = sorted(distances, key=lambda x: x['distance'])
    return  sorted_dist[0:n]

def create_product_text(product):
    return f"""Title: {product['title']}
    Description: {product['short_description']}
    Category: {product['category']}
    Features: {', '.join(product['features'])}"""

def find_closest(query_vector, embdeddings):
    distances = []
    for i, embedding in enumerate(embdeddings):
        dist = distance.cosine(query_vector, embedding)
        distances.append({"distance": dist, "index": i})
    return min(distances, key=lambda x:x['distance'])