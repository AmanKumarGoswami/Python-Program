# Python program to find root of a quadratic equation.
from math import sqrt
a = int(input("Enter the value of a of quadratic equation : "))
b = int(input("Enter the value of b of quadratic equation : "))
c = int(input("Enter the value of c of quadratic equation : "))
discriminant = (b*b) - (4*a*c)

if(discriminant > 0):
    root1 = (-b + sqrt(discriminant) / (2 * a))
    root2 = (-b - sqrt(discriminant) / (2 * a))
    print("Two Distinct Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
elif(discriminant == 0):
    root1 = root2 = -b / (2 * a)
    print("Two Equal and Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
elif(discriminant < 0):
    root1 = root2 = -b / (2 * a)
    imaginary = sqrt(-discriminant) / (2 * a)
    print("Two Distinct Complex Roots Exists: root1 = %.2f+%.2f and root2 = %.2f-%.2f" %(root1, imaginary, root2, imaginary))
