#Python program to find largest of two numbers

x=int(input("Enter the value of first number :"))
y=int(input("Enter the value of second number :"))
if x>y:
    print(x," is greater.")
elif y>x:
    print(y," is greater.")
else:
    print("Equal value...",x)

#if x==y:
#    print("Equal")
#else:
#   larger=x if x>y else y
#    print("{0} is greater.".format(larger))