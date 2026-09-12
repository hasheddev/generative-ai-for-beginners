from langchain_huggingface import HuggingFacePipeline
from langchain_openai import ChatOpenAI
import os
from pydantic import SecretStr

llm = ChatOpenAI(model="gpt-4o-mini", api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""))

prompt = 'Three reasons for using LangChain for LLM application development.'
response = llm.invoke(prompt)

print(response.content)

llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20}
)

prompt = "Hugging Face is"

# Invoke the model
response = llm.invoke(prompt)
print(response)