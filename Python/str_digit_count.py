import re

#Count the number of digits in a given string.

text = "The 2019 batch passed from CSC dept, ECE dept are 117, 210 with an average of 75%"

dig_cnt = 0

print(text)
#print(re.match(r"\d",text))
#found = bool(re.search(r"\d",text))
#print(found)

for i in range(len(text)):
    found = bool(re.search(r"\d",text[i]))
    if found:
       dig_cnt = dig_cnt + 1
       print("index ",i)

print("total count ",dig_cnt)

