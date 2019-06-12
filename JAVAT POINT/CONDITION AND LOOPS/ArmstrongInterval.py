#Python program to print Armstrong number in a given interval.

def armStrong(lower, upper):
    for i in range(lower, upper+1):
        num = i
        s = 0
        n = len("i")
        while i>0:
            temp = i % 10
            s = s + temp**n
            i //= 10
        if num == s:
            print(num, "is an Armstrong number.")
        else:
            print(num, "is not an Armstrong number.")

l = int (input("Enter the lower limit : "))
u = int (input("Enter the upper limit : "))
armStrong(l ,u)

    

