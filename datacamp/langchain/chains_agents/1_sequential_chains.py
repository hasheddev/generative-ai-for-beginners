from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from pydantic import SecretStr

llm = ChatOpenAI(model="gpt-4o-mini", api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""))

learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

# Create a prompt template that places a time constraint on the output
time_prompt = PromptTemplate(
    input_variables=['learning_plan'],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}."
)

# Invoke the learning_prompt with an activity
print(learning_prompt.invoke({"activity": "chess"}))

seq_chain = ({"learning_plan": learning_prompt | llm | StrOutputParser()}
    | time_prompt
    | llm
    | StrOutputParser())

# Call the chain
print(seq_chain.invoke({"activity": "chess"}))