#Python program to check entered number is an Armstrong number or not.

def armStrong(num):
    s = 0
    n = len("num")
    print(n)
    while num<0:
        temp = num % 10
        s = s + temp**n
        num = num % 10
    return s

n = int (input("Enter the number to be checked : "))
l = armStrong(n)
if n == l:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
