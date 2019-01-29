# Python program to find whether the number is divisble by 5 and 11.

num = int(input("Enter the number :"))
if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible by both 5 and 11.")
elif num % 5 == 0:
    print(num, "is divisible by 5 only.")
elif num % 11 == 0:
    print(num, "is divisible by 5 only.")
else:
    print(num, "is not divisible by both 5 and 11.")
