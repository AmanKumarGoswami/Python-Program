# Python program to check whether the entered number is palindrome or not
sum = 0
number = int(input("Enter the number to be checked :"))
num = number
while num > 0:
    n = num % 10
    sum = sum * 10 + n
    num = num // 10

if sum == number:
    print(number, "is a palindrome number.")
else:
    print(number, "is not a palindrome number.")
