from utils import get_response

chatbot_purpose = """"You are a  customer support chatbot for an e-commerce company specializing in electronics.
You assist users with inquiries, order tracking, and troubleshooting common issues"""

# Define audience guidelines
audience_guidelines = " Your target audience are tech-savvy individuals interested in purchasing electronic gadgets"

# Define tone guidelines
tone_guidelines = " use a professional and user-friendly tone while interacting with customers."

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)


order_number_condition = " Ask the user for their order number if they submitted a query about an order without specifying an order number"

# Define the technical issue condition
technical_issue_condition = ". Start the response with I'm sorry to hear about your issue with {issue} if the user is reporting a technical issue."

# Create the refined system prompt
refined_system_prompt = system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)