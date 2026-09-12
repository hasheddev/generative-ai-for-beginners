from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
import os
from pydantic import SecretStr
import pandas as pd

data = {
    "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "name": [
        "Tech Innovators Inc.",
        "Green Solutions Ltd.",
        "Global Enterprises",
        "Peak Performance Co.",
        "Visionary Ventures",
        "NextGen Technologies",
        "Dynamic Dynamics LLC",
        "Infinity Services",
        "Eco-Friendly Products",
        "Future Insights",
    ],
    "subscription_type": [
        "Premium",
        "Standard",
        "Basic",
        "Premium",
        "Standard",
        "Basic",
        "Premium",
        "Standard",
        "Basic",
        "Premium",
    ],
    "active_users": [450, 300, 150, 800, 600, 200, 700, 500, 100, 900],
    "auto_renewal": [True, False, True, True, False, True, True, False, True, True],
}

customers = pd.DataFrame(data)

llm = ChatOpenAI(model="gpt-4o-mini", api_key=SecretStr(os.getenv("OPENAI_API_KEY") or ""))

def retrieve_customer_info_raw(name: str) -> str:
    """Retrieve customer information based on their name."""
    # Filter customers for the customer's name
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()

# Call the function on Peak Performance Co.
print(customers)
print(retrieve_customer_info_raw("Peak Performance Co."))

@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    # Filter customers for the customer's name
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()


tools = [retrieve_customer_info]

#Define the agent
agent = create_react_agent(llm, tools)

print(retrieve_customer_info.args)

messages = agent.invoke({"messages": [("human", "Create a summary of our customer: Peak Performance Co.")]})
print(messages['messages'][-1].content)