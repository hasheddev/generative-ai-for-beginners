from utils import get_response
#text analysis and entity extraction   assign category to text
ticket = """
Subject: Urgent - Login Error
    
    Hi Support Team,
    
    I'm having trouble accessing my account with the username "example_user." Every time I try to log in, I encounter an error message. I've already attempted to reset my password, but the issue persists. I need to resolve this problem urgently, as I have pending tasks that require immediate attention.
    
    Please investigate and assist promptly.
    
    Thanks,
    John.
"""
prompt = f"""classify the text in the backtick as  technical issue, billing inquiry, or product feedback give just the classification ```{ticket}```"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)

ticket_4 = """
 Greetings, I am facing technical difficulties with your software, ABC Editor. My name is Sarah Lee, and I recently upgraded to the latest version. However, whenever I try to save my work, the software crashes. Can you please help me resolve this problem?"""

prompt = f""""
Ticket: ->  Entities:
Ticket: ->  Entities: 
Ticket: ->  Entities:
Ticket: {ticket_4} ->  Entities: """

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)
