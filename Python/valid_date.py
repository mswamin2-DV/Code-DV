import re

#Validate if a string represents a valid date in the format "YYYY-MM-DD".

text = "2024-1-4"

pattern = r"^\d{4}-[0-1]*[0-2]+-[0-3]*[0-9]+$"

print(re.match(pattern,text))