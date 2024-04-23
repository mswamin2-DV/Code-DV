import re

#Validate if a string represents a valid IPv4 address.

def valid_ip(word):
    
    #pattern = r"^([0-2]*[0-5]*[0-5]+\.){3}[0-2]*[0-5]*[0-5]$"
    pattern = r"^([0-2]*[0-5]{1,2}\.){3}[0-2]*[0-5]{1,2}$"
    return re.match(pattern,word)


word = "255.255.255.0"
print(valid_ip(word))