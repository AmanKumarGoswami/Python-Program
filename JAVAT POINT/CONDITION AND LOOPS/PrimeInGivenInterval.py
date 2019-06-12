# Python program to print all prime numbers in an interval

def prime(start, end):
    for i in range (start, end+1):
        if i>1:
            for j in range(2, int(i/2)+1):
                if i%j==0:
                    break 
            else:
                print(i)                
start = int(input("Enter the starting point : "))
end = int(input("Enter the ending point : "))

print(prime(start,end))


