"""
67) How can you pick a random item from a range? 
"""

import random

start = int(input("Enter Start Range : "))
end = int(input("Enter End Range : "))
r = []
for i in range(start,end+1):
    r.append(i)

pick = random.choice(r)

print(f"Pick : {pick}")