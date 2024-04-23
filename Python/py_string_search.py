import re

#Check if a string contains a specific word.

text = "Hello! It is a Free country in a freeworld in a free universe"

word = "free"


#method-1
pattern = r"\b" + word + r"\b"
print(re.search(pattern,text))
    
#method-2
#print("free" not in text.lower())  #to make case insensitive use lower

#method-3
"""if "free" in text:
    print("free is present")
else:
    print("free is not present")"""