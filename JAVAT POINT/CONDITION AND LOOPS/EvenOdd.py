#Python program to check entered number is even or odd.

def evenOdd(num):
    if num%2==0:
        return 1

n = int(input("Enter the number to be checked : "))
if evenOdd(n) ==True:
    print("Even Number.")
else:
    print("Odd number.")
