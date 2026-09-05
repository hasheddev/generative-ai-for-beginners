from utils import calculate_closeness, create_embeddings, get_min_index

#0 to 2  smaller == closer

short_text = ''
list_description = []

products = []

short_embedding = create_embeddings(short_text)[0]
list_description_embedding = create_embeddings(list_description)

search_text = "soap"
search_embedding = create_embeddings(search_text)[0]

distances = []
for product in products:
  dist = calculate_closeness(search_embedding, product['embedding'])
  distances.append(dist)
  
min_dist_ind = get_min_index(distances)
print(products[min_dist_ind]['short_description'])