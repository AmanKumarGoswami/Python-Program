#Python program to find largest of three

x=int(input("Enter the value of first number :"))
y=int(input("Enter the value of second number :"))
z=int(input("Enter the value of third number :"))

if x==y==z:
    print("All numbers have same value.")
else:
    larger=x if x>y and x>z else y if y>x and y>z else z
    print("{0} is greater.".format(larger))