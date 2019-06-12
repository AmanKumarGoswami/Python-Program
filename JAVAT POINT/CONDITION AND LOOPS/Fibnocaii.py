#Python program to print fibnocaii series.

def fib(num):
    first = 0
    print("0")
    second = 1
    print("1")
    for i in range (0, num-2):
        s = first + second
        print(s)
        first = second
        second = s
    return

n = int(input("Enter the number : "))
fib(n)
