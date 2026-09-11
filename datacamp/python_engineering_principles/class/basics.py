from collections import Counter

def tokenize(text: str):
  return text.split()

class NDocument:
  def __init__(self, text):
    self.text = text
    # pre tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # pre tokenize the document with non-public count_words
    self.word_counts = self._count_words()

  def _tokenize(self):
    return tokenize(self.text)
	
  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)

# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of Document
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text

