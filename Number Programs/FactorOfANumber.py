# python program to find factor of a  number

number = int(input("Enter the number :"))
print("Factors of a given numbers :")
for i in range(1, number+1):
    if number % i == 0:
        print("{0}".format(i), end=" ")
