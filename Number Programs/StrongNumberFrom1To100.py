# Python program all strong numbers from 1 to 100.


for i in range(1, 101, 1):
    sum = 0
    number = i
    while i > 0:
        temp = i % 10
        fact = 1
        for k in range(1, temp+1):
            fact = fact * k
        sum = sum + fact
        i = i // 10
    if sum == number:
        print(number, "is a Strong")
    else:
        print(number, "is Not a strong.")
