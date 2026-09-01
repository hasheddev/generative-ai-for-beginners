from .utils import get_response

#Tables, list, paragraphs

# Create a prompt that generates the table
prompt = "generates a table of 10 books, with columns for Title, Author, and Year, that you should read given that you are a science fiction lover."

# Get the response
response = get_response(prompt)
print(response)


text = """```The sun was setting behind the mountains, casting a warm golden glow across the landscape. Birds were chirping happily, and a gentle breeze rustled the leaves of the trees.
It was a perfect evening for a leisurely stroll in the park```"""

# Create the instructions
instructions = "determine language of the text in the triple backticks and generate a suitable title for it"

# Create the output format
output_format = f" The output sould include the text, language and title on separate lines with prefices 'Text:', 'Language:' and 'Title:'   ```{text}```"

# Create the final prompt
prompt = instructions + output_format
response = get_response(prompt)
print(response)

text = "The sun was setting behind the mountains, casting a warm golden glow across the landscape."

instructions = "infer the language and the number of sentences of the given delimited text; then if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title"

# Create the output format
output_format = "include the text, language, number of sentences, and title, each on a separate line,and ensure to use 'Text:', 'Language:', and 'Title:' as prefixes for each line."

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)