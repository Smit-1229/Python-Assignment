"""
41) Write a Python program to check whether a list contains a sub list

"""

list_main = [10,20,30,40]
sub_list = [20,30]
contains = False
#check wheather sub string is there in main list
m,n = len(list_main),len(sub_list)

if n == 0 :
    contains = True
elif m >= n :
    for i in range(m-n+1):
        if list_main[i:i+n] == sub_list:
            contains = True
            break

#Print Result
if contains:
    print("The sub list is present in main list")
else:
    print("The sub list is not present in main list")
    