#34.Write a Python program that simulates an online shopping checkout, checkingproduct availability and user wallet balance.
price = 4000
avail = True  

wallet = int(input("Enter wallet balance: "))

if avail == True:
    if wallet >= price:
        print("Order placed successfully")
        print("Remaining balance:", wallet - price)
    else:
        print("Insufficient wallet balance")
else:
    print("Product out of stock")
