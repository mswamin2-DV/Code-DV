import re 

with open(r"c:/Users/Mathura Swaminathan/Coding practice/1/Document1.txt", 'r') as f:
    #lines = f.readlines()
    for l_no, line in enumerate(f):
        #print(re.search(r"^w",line))
        print(re.search(r"^([a-z]+[0-9]+)|([0-9]+[a-z]+)$",line)) 
