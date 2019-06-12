# Python program to make a simple calculator.

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b

num = int(input("Enter the first number :"))
num1 = int(input("Enter the second number : "))

print("\nSelect your option : ")
print("1 for addition.")
print("2 for subtration.")
print("3 for multiplication.")
print("4 for division.\n")

chs = int(input("Enter your choice :"))

if chs == 1:
    print("Addition of ",num,"+ ",num1,"= ",add(num, num1))

elif chs == 2:
    print("Subtraction of ",num,"- ",num1,"= ",sub(num, num1))
    
elif chs == 3:
    print("Multiplication of ",num,"* ",num1,"= ",mult(num, num1))
    
elif chs == 4:
    print("Division of ",num,"/ ",num1,"= ",div(num, num1))

else:
    print("Wrong choice!")
























    

