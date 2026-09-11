# import the numpy package
import numpy as np
# load the Counter function into our environment
from collections import Counter

# create an array class object
arr = np.array([8, 6, 7, 5, 3, 0, 9])

# use the sort method
arr.sort()

# print the sorted array
print(arr)

#pypi python package index        pip - pip installs packages

# View the documentation for Counter.most_common
help(Counter.most_common)
words = ['DataCamp']
top_5_words = Counter(words).most_common(5)

# display the top 5 most common words
print(top_5_words)
