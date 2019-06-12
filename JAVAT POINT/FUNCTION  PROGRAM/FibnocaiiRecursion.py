# Python program to find factorial of a given number using recursion.

def fib(num):
    if num <= 1:
        return num
    else:
        return (fib(num-1) + fib(num-2)) 

n = int(input("How many terms : "))
print("Fibonacci series :")
for i in range(n):  
       print(fib(i),end = ' ') 
