from openai import OpenAI

#response.choices[0].finish_reason == 'tool_calls'


function_definition = [
        {
        "type": "function",
        "function": {
            "name": "get_exchange_rate",
            "description": "gets the exchange rate for a currency",
            "parameters": {
                "type": "object",
                "properties": {
                    "currency_code": {
                        "type": "string",
                        "description": "currency code of currency to get exchange rate",
                    }
                },
                "required": ["currency_code"],
            },
            "result": {
                "type": "string",
            },
        },
    }
]

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant and currency exchange specialist. "
            "Your role is to analyze user requests about currencies, identify "
            "the target currency, and extract its standard 3-letter ISO code "
            "(e.g., 'EUR', 'USD', 'GBP') to pass as the 'currency_code' argument "
            "when calling functions."
        ),
    },
    {
        "role": "user",
        "content": "I'd like to know the current exchange rates for the Euro.",
    },
]

# if response.choices[0].finish_reason=='tool_calls':
#   function_call = response.choices[0].message.tool_calls[0].function
#   # Check function name
#   if function_call.name == 'get_exchange_rate':
#     # Extract currency code
#     code = json.loads(function_call.arguments)["currency_code"]
#     exchange_info = get_exchange_rate(code)
#     print(exchange_info)
#   else:
#     print("Apologies, I couldn't find the requested currency.")
# else: 
#   print("I am sorry, but I could not understand your request.")