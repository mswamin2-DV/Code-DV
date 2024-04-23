import re

#Extract all words starting with a specific prefix from a string.

text = "Recently they were reciprocated by the respectable wrestler"

prefix = "re"

#pattern = r"\b"+prefix+r"[^ ]*\b"
pattern = r"\b"+prefix+r"\S*\b"

print(re.findall(pattern,text.lower()))