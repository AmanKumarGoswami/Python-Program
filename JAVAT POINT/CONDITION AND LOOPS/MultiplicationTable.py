#Python program to print table of a given number.

def table(num):
    for i in range (1, 11):
        #ans = num * i
        print("{0} * {1}= {2}".format(num, i, num*i))
    return

number = int (input("Enter the number : "))
table(number)
