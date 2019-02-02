# Python program to find sum of digits of a number.

sum = 0
number = int(input("Enter the number :"))

while number > 0:
    num = number % 10
    sum = sum + num
    number = number // 10
print("Sum of digits of a number is", sum)
