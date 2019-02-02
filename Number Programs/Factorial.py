# python program to find factorial number

number = int(input("Enter the number :"))
factorial = 1
for i in range(1, number+1):
    factorial = factorial * i
print("Factorial of a number : {0}".format(factorial))
