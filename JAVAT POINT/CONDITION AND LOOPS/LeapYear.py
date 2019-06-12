#Python program to Check weather the entered year is leap year or not.

def chk(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 == 0:
        return True

year = int(input("Enter the year to be checked :"))
if chk(year) == True:
    print('Leap Year.')
else:
    print('Not a Leap Year.')
    
