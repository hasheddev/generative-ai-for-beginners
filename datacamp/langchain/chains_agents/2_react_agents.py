from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools
import os
from pydantic import SecretStr

llm = ChatOpenAI(model="gpt-4o-mini", api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""))
tools = load_tools(["wikipedia"], llm=llm)

# Define the agent
agent = create_react_agent(llm, tools)

# Invoke the agent
response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})
print(response['messages'][-1].content)
#Reason Act