import re

# Replace all occurrences of a word with another word in a string.

text = "Hello! It is a free country in a free world in a freeuniverse"

word = "free"

pattern = r"\b" + word + r"\b"

print(re.sub(pattern,"captive",text))