#Python program to check whether the entered number is positive or negative.

num=int(input("Enter the number to be checked :"))

if num>0:
    print(num, "is positive.")
elif num<0:
    print(num,"is negative.")
else:
    print("Zero.")