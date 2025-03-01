"""
78) Write a python program to find the longest words.
"""

def find_longest_word_in_file(file_name):
    with open(file_name, "r") as file :
        words = file.read().split()
        longest_word = max(words,key=len)
        return longest_word

file_name = "Sample_3"

longest_word =find_longest_word_in_file(file_name)

print(f"Longest word in file is '{longest_word}'!!")