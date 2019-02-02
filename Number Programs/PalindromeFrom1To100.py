# Python program to print all palindrome number from 1 to 100

for i in range(1, 101):
    sum = 0
    num = i
    while num > 0:
        n = num % 10
        sum = sum * 10 + n
        num = num // 10

    if sum == i:
        print(i, "is a palindrome number.")
