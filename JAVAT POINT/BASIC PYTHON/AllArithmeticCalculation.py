# Python program to perform arthimetic calculation.


def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b
def modu(a, b):
    return a%b

a = int(input("Enter the first number : "))
b = int(input("Enter the first number : "))
print(add(a, b))
print(sub(a, b))
print(mult(a, b))
print(round(div(a,b), 2))
print(modu(a, b))


