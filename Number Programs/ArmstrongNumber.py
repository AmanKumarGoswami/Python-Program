# Python program to check weather the entered number  is an armstrong number or not
from math import pow
sum = count = 0
number = int(input("Enter the number to be checked :"))
n = num = number
while num > 0:
    temp = num % 10
    count = count + 1
    num = (num-temp)/10

while number > 0:
    temp1 = number % 10
    power = pow(temp1, count)
    sum = sum + power
    number = (number-temp1) / 10

if n == sum:
    print(n, "is an armstrong number.")
else:
    print(n, "is not an armstrong number.")
