"""
63) Write a Python function to check whether a number is perfect or not. 
"""
def check_num_perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    
    if sum == num :
        return f"The Number({num}) is a perfect number."
    else:
        return f"The Number({num}) is not a perfect number"
        
num = int(input("Enter A Number : "))

ans = check_num_perfect(num)

print(ans)
        