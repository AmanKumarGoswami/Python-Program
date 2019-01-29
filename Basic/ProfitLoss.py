#Python program for profit or loss.

purchasePrice=int(input("Enter the Purchase price:"))
salesPrice=int(input("Enter the Sales price:"))
cal=salesPrice-purchasePrice
if cal>0:
    print("Profit of ",cal)
elif cal<0:
    print("Loss of ",cal)
else:
    print("No profit No loss!!!")