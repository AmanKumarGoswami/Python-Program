# Python program to find power of a number.
answer = 1
number = int(input("Enter the number :"))
power = int(input("Enter the exponential value:"))

for i in range(1, power+1):
    answer = answer*number
print("{0} ^ {1} : {2}".format(number, power, answer))
