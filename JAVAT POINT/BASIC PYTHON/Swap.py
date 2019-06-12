# Python program to swap two number

def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return (a, b)

x = int(input("Enter the value for a : "))
y = int(input("Enter the value for b : "))

print("The value of a and b before swapping are : ", x, y)
print("The value of a and b after swapping are : ",swap(x, y))
