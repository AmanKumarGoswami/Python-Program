# python program to find first digit of a number

number = int(input("Enter the number here :"))
while number > 10:
    number = number // 10
    first = number
print("First digit of a number {0}".format(first))

