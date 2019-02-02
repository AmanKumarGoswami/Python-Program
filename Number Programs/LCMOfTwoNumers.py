# python program to find LCM of two numbers.
lcm = 1
first = int(input("Enter the value of first number :"))
second = int(input("Enter the value of second number :"))
if first > second:
    num = first
else:
    num = second
while(True):
    if(num % first == 0 and num % second == 0):
        print("\n LCM of {0} and {1} = {2}".format(first, second, num))
        break
    num = num + 1
