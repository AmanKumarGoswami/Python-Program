#Python program to print all odd number from 1 to N.

N=int(input("Enter the value of N :"))

for x in range(1,N+1):
    if x%2!=0:
        print(x,end=" ")