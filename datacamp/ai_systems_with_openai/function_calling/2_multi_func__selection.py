from openai import OpenAI
#used to extract structured data and conncet to external tools and apps
#system propmt   extraact based on user input

function_definition = [
    {
        'type': 'function',
        'function': {
            'name': 'real_estate_info',
            'description': 'Get the information about homes for sale from the body of the input text',
            'parameters': {
                'type': 'object', 
                'properties': {
                    'home type': {
                        'type': 'string', 'description': 'Home type'
                        },
                    'location': {
                        'type': 'string', 'description': 'Location'
                        },
                        'price': {
                            'type': 'integer', 'description': 'Price'
                            },
                        'bedrooms': {
                            'type': 'integer', 'description': 'Number of bedrooms'
                            }
                    }
                }
            }
    }
]

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function_definition.append({'type': 'function', 'function':{'name': 'reply_to_review', 'description': 'returns response to user review as a reply property', 'parameters': {'type': "object", 'properties': {'reply': {'type': 'string', 'description': 'reply to user review' }}}}})
message_listing =[]

response = response= client.chat.completions.create(
    model="gpt-4o-mini",
    # Add the message
    messages=message_listing,
    # Add your functigeson definition
    tools=function_definition
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

model = "gpt-4o-mini"

response= client.chat.completions.create(
    model=model,
    messages=message_listing,
    # Add the function definition
    tools=function_definition,
    # Specify the function to be called for the response
    tool_choice={'type': 'function',  "function": {"name": "extract_review_info"}}  #'auto default
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

message_listing.append({'role': 'system', 'content': 'Do not assume any values for any responses and return only values from input'})