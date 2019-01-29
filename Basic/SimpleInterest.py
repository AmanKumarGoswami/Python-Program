# Python program to calculate simple interest
princ_amt = float(input("Enter the principal amount :"))
rate_of_int = float(input("Enter the rate of interest :"))
time_period = float(input("Enter the time period :"))

print("Simple interest : {0}".format((princ_amt*rate_of_int*time_period)/100))
