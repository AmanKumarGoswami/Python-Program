# Python program to print sum of natural numbers.

def natSum(num):
    Sum = 0
    for i in range (1, num+1):
        Sum = Sum + i
    return Sum

n = int(input("Enter the number : "))
print("Sum of n numbers", natSum(n))
