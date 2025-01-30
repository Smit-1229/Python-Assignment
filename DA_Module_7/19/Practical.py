"""
19) Write a Python program to count the occurrences of each word in a Given sentence. 
"""
string = input("Enter A Sentence : ")

words = string.split()


words_count = {}

for w in words :
    word = w.capitalize()
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
        
for word,count in words_count.items():
    print(f" {word} : {count}")
    