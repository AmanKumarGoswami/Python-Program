# Python program to find the solution of a quadratic solution.
import cmath
a = int(input("Enter value for a :"))
b = int(input("Enter value for b :"))
c = int(input("Enter value for c :"))

d=(b**2)/(4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("Solution of quadratic equation are {0} and {1}".format(sol1, sol2))
