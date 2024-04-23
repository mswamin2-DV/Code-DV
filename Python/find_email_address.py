
import re

#Extract all email addresses from a given text.

def str_search(text):
    return re.findall(r"\b[a-zA-Z0-9_]+@[a-zA-Z]+.[A-Z|a-z]\b",text)

text = "Hi, how are you? I would like to share my email ab_cd@gmail.com. You could also reach me at xyz123@hotmail.ORG or pqr@yahoo.in"
print(str_search(text))
    
