# Python program to print table of a given number.

num = int(input('Enter the number here :'))
for i in range(1, 11):
    print("{0} * {1} = {2}".format(num, i, num*i))
