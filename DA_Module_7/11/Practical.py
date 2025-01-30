#Write a Python program to test whether a passed letter is a vowel or not. 

char = input("Enter a simgle letter : ").strip()

vowel = {"a","e","i","o","u"}

if len(char) == 1 and char.isalpha():
    if char.lower() in vowel :
        print(f"{char} is a vowel")
    else:
        print(f"{char} is not a vowel")
else:
    print("Enter a valid input for check")
