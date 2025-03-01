"""
62) Write a Python function to check whether a number is in a given range
"""

def num_in_range(num,start,end):
    if start <= num <= end:
        return f'Yes! The {num} is in the range({start}-{end})'
    else:
        return f'No! The  {num} is not in the range({start}-{end})'
    
num = int(input("Enter Num : "))
start = int(input("Enter Range Starting : "))
end = int(input("Enter Range End : "))

ans = num_in_range(num,start,end)

print(ans)