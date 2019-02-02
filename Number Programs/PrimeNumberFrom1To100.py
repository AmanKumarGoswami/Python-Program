# Python program to find out all prime numbers from 1 to 100.

for i in range(2, 101, 1):
    for j in range(2, (i+1)//2, 1):
        if i % j == 0:
            break
    else:
        print(i, "is a prime number.")
