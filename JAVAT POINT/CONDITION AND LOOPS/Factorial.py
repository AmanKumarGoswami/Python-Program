#Python program to find factorial of a number

def fact(num):
    fact = 1
    for i in range(num ,0,-1):
        fact = fact * i
    return fact

n = int(input("Enter the number : "))
print("Factorial of a number : ", fact(n))
