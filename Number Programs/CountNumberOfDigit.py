# python program to find number of digits in a number.

count = 0
num = int(input("Enter the number :"))

while num > 0:
    count = count + 1
    num = num//10
print(count)
