"""
58) Write a Python program to combine values in python list of dictionaries. 
    Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] 
    Expected Output: 
        • Counter ({'item1': 1150, 'item2': 300}) 
"""

data = [{'item' : 'item1', 'amount' : 400}, 
        {'item' : 'item2', 'amount' : 300},
        {'item' : 'item1', 'amount' : 750}
        ]

result = {}

for i in data :
    key = i['item']                                                     # the item  is taken
    if key in result:                                                   #check the iem is in relult or not                          
        result[key] += i['amount']
    else:
        result[key] = i['amount']

print(f" counter ({result})")