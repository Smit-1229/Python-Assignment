"""
60) Sample string:
 'w3resource' 
 Expected output: 
• {'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 

"""

string = 'w3resource'

count_Char = {}

for char in string:
    if char.lower() in count_Char:
        count_Char[char] += 1
    else:
        count_Char[char] = 1


    
print(count_Char)