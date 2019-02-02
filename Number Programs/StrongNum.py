# Python program to find out whether the entered number is a strong number or not.

number = int(input("Enter the number to be checked :"))
num = number
sum = 0

while num > 0:
    temp = num % 10
    fact = 1
    for i in range(1, temp+1):
        fact = fact * i
    sum = sum + fact
    num = num // 10
if sum == number:
    print(number, "is a Strong")
else:
    print(number, "is Not a strong.")
