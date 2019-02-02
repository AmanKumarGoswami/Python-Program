# Python program to reverse a number.

rev = 0
num = int(input("Enter the number to be checked :"))
number = num
while num > 0:
    n = num % 10
    rev = rev * 10 + n
    num = num // 10
print("Reverse of a number {0} : {1}".format(number, rev))

