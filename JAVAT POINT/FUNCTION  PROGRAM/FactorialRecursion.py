# Python program to find the factorial of a number using recursion.

def fact(num):
    
    if num<1:
        return 1
    else:
        num = num * fact(num-1)
        return num

n = int(input("Enter the number : "))
print("Factorial of a given number : ", fact(n))
