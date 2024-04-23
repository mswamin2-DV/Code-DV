import re

#Extract all words containing at least one uppercase letter from a string.

text = "The 2019 batch passed from CSC dept, ECE dept are 117, 210 with an average of 75%"

pattern = r"\b\S*[A-Z]\S*\b"

print(re.findall(pattern,text))

