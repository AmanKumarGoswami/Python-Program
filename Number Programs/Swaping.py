# Python program to swap two numbers

a = int(input("Enter the value of first number :"))
b = int(input("Enter the value of second number :"))

t = a
a = b
b = t

print("After swapping value of first variable :{0} \n value of second variable : {1}".format(a, b))
