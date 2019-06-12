#Python program to check wether a number is positive, Negative or Zero.


def check(num):
    if num > 0:
        return True
    elif num < 0:
        return False

n = int(input("Enter the number to be checked : "))
if check(n) == True:
    print("Positive.")
elif check(n)== False:
    print("Negative.")
else:
    print("Zero.")
