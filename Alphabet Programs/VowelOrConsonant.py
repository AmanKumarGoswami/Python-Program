# Python program to check whether the entered character is a vowel or consonant.

ch = input("Enter the character to be checked :")[0]
if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U' :
    print(ch, "is a vowel character.")
elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <='Z'):
    print(ch, "is a consonant character.")
else:
    print(ch, "is not a character.")
