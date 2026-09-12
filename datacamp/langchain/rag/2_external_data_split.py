from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredHTMLLoader

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap)

# Split the string and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap)

# Split the document and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])

# Load the HTML document into memory
loader = UnstructuredHTMLLoader("white_house_executive_order_nov_2023.html")
data = loader.load()

# Define variables
chunk_size = 300
chunk_overlap = 100
# Split the HTML
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=['.'])

docs = splitter.split_documents(data)
print(docs)