"""
35) Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.
"""
list_1 =[]
for i in range(1,31):
    list_1.append(i*i)

result = list_1[:5] + list_1[-5:-1]

print(f"The list of first and last 5 elements is {result}")
