# Python program to find entered character is in upper or lower case.

ch = input("Enter the character to be checked :")[0]
if ch >= 'A'and ch <= 'Z':
    print(ch, 'is a upper case character.')
elif ch >= 'a' and ch <= 'z':
    print(ch, 'is a lower case character.')
else:
    print(ch, 'is neither upper case nor lower case character.')
