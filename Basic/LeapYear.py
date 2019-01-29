#Python program to find whether the given year is leap year or not

year=int(input("Enter the year to be checked :"))

if year%4==0 or year%400==0 and year%100!=0:
    print(year," is leap year.")
else:
    print(year," is not a leap year.")