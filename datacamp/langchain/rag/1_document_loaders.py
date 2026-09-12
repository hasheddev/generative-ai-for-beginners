from langchain_community.document_loaders import CSVLoader, PyPDFLoader, UnstructuredHTMLLoader

loader = PyPDFLoader("rag_vs_fine_tuning.pdf")

# Load the document
data = loader.load()
print(data[0])

loader = CSVLoader("fifa_countries_audience.csv")

# Load the document
data = loader.load()
print(data[0])

loader = UnstructuredHTMLLoader('white_house_executive_order_nov_2023.html')

# Load the document
data = loader.load()

# Print the first document
print(data[0])

# Print the first document's metadata
print(data[0].metadata)