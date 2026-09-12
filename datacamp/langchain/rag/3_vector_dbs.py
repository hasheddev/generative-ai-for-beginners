from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os
from pydantic import SecretStr

loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

# Split the document using RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50)
docs = splitter.split_documents(data) 

llm = ChatOpenAI(model="gpt-4o-mini", api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""))

# Embed the documents in a persistent Chroma vector database
embedding_function = OpenAIEmbeddings(api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""), model='text-embedding-3-small')

vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding_function,
    persist_directory=os.getcwd()
)

# Configure the vector store as a retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

message = """
Answer the following question using the context provided:

Context:
{context}

Question:
{question}

Answer:
"""

# Create a chat prompt template from the message string
prompt_template = ChatPromptTemplate.from_messages([("human", message)])

rag_chain = ({"context": retriever, "question": RunnablePassthrough()}
            | prompt_template
            | llm)

# Invoke the chain
response = rag_chain.invoke("Which popular LLMs were considered in the paper?")
print(response.content)