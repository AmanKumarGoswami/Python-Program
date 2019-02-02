# Python program to check whether the entered number is prime or not

number = int(input("Enter the number to be checked :"))
for i in range(2, (number+1)//2, 1):
    if number % i == 0:
        print(number, "is not prime number.")
        break
else:
    print(number, "is a prime number.")
