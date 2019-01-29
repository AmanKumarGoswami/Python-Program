#Python program to print sum and average of all natural numbers from 1 to N

N=int(input("Enter the value of N :"))
sum=0
for x in range(1,N+1):
    sum=sum+x
print("Sum of all natural numbers from 1 to {0} : {1}".format(N,sum))
average=sum/N
print("Average of all natural numbers from 1 to {0} : {1}".format(N,average))
