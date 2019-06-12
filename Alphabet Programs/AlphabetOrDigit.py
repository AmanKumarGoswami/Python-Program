# Python program to find entered character is an alphabet or a digit.

char = input("Enter the character to be checked :")[0]
if (char >= 'A' and char <= 'Z') or (char >='a' and char<='z'):
    print(char, "is a character.")
elif (char >= '0' and char <= '9'):
    print(char, "is a digit.")
else:
    print(char, "is neither a character nor a digit.")
