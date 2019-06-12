#Python program to check wether the entered number is prime or not.

def prime(num):
    for i in range(2,int(num/2)):
        if num % i == 0:
            return True

number = int(input("Enter the number to be checked :"))
if prime(number) == True:
    print("Not a prime number.")
else:
    print("Prime number.")

