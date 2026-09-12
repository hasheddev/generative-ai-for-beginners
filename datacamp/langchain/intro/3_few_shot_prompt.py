from langchain_openai import ChatOpenAI
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
import os
from pydantic import SecretStr

llm = ChatOpenAI(model="gpt-4o-mini", api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""))

# Create the examples list of dicts
examples = [
  {
    "question": "How many DataCamp courses has Jack completed?",
    "answer": "36"
  },
  {
    "question": "How much XP does Jack have on DataCamp?",
    "answer": "284,320XP"
  },
  {
    "question": "What technology does Jack learn about most on DataCamp?",
    "answer": "Python"
  }
]

example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

# Create the few-shot prompt
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

prompt = prompt_template.invoke({"input": "What is Jack's favorite technology on DataCamp?"})
print(prompt.to_string())

llm_chain = prompt_template | llm
print(llm_chain.invoke({"input": "What is Jack's favorite technology on DataCamp?"}))