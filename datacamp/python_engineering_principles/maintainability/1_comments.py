import re

def greet_user(name, clean=False):
    """Format a friendly greeting message for a user.

    Args:
        name (str): The name of the user to greet.
        clean (bool): If True, strip whitespace from the name. Defaults to False.

    Returns:
        str: The generated greeting message.
    """
    if clean:
        name = name.strip()
    return f"Hello, {name}!"


def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall 
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ["the", "rain", "in", "spain"]
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize)