#Python program to find lcm of a number.

def lcm(first, second):
    if first > second:
        grt = first
    else:
        grt = second

    while True:
        if (grt%first==0) and (grt%second==0):
            return grt
        else:
            grt+=1

p = int(input("Enter the value of first number :"))
q = int(input("Enter the value of second number :"))

print("Least common multipal of ",p,"and",q,":",lcm(p, q))
