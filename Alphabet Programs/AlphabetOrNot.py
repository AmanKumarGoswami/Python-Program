# Python program to check whether the entered character is an alphabet of not.

char = input("Enter the character to be checked :")[0]
if (char >= 'A' and char <= 'Z') or (char >='a' and char<='z'):
    print(char, "is a character.")
else:
    print(char, "is not a character.")
