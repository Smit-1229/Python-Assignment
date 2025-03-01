"""
80) Write a Python program to count the frequency of words in a file. 
"""

def count_words_in_file(file_name):
    with open(file_name, "r") as file:
        words = file.read().split()
        count_word = {}
        for word in words:
            if word in count_word:
                count_word[word] += 1
            else:
                count_word[word] = 1
        
        return count_word

file_name = "Sample_3"

count_word = count_words_in_file(file_name)

print(count_word)
