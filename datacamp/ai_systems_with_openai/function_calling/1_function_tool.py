from openai import OpenAI
#used to extract structured data and conncet to external tools and apps

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

message_listing =[]

response= client.chat.completions.create(
    model="gpt-4o-mini",
    # Add the message
    messages=message_listing,
    # Add your functigeson definition
    tools=function_definition
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

def extract_dictionary(response):
  return response.choices[0].message.tool_calls[0].function.arguments

# Print the data dictionary
print(extract_dictionary(response))

