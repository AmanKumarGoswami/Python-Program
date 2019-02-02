# Python program to find whether the entered number is perfect or not.

number = int(input("Enter the number to be checked :"))
num = number
sum = 0
for i in range(1, number+1//2):
    if number % i == 0:
        sum = sum + i
if sum == number:
    print(sum, " is a Perfect number.")
else:
    print(sum, "is Not a perfect number.")
