# Python program to find out the compound intrest

import math
princ_amount = int(input("Enter the Principal amount :"))
rate_of_int = int(input("Enter the rate of interest :"))
time_period = int(input("Enter the time period :"))

ci_future = princ_amount * (math.pow((1 + rate_of_int / 100),time_period))
compound_int = ci_future - princ_amount

print("Future Compound Interest for Principal Amount {0} = {1}".format(princ_amount, ci_future))
print("Compound Interest for Principal Amount {0} = {1}".format(princ_amount, compound_int))