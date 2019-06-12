# Python program to find HCF of two numbers.

def hcf(first, second):
    if first > second:
        sml = second
    else:
        sml = first

    for i in range (1, sml+1):
        if first%i == 0 and second % i ==0 :
            gcf = i
    return gcf

p = int(input("Enter the vslue of first number : "))
q = int(input("Enter the value of second number : "))

print("Higest common factor : ", hcf(p, q))
