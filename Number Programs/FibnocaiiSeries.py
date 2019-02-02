# python program to generate fibonacci series upto N.
sum = 0
first = 0
second = 1
N = int(input("Enter the number :"))
for i in range(0, N):
    if (i <= 1):
        sum = i
    else:
        sum = first + second
        temp = first
        first = second
        second = sum
    print(sum, end=" ");
