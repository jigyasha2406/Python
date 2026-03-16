#Write a Python program that simulates an ATM withdrawal system, where theprogram checks account balance, minimum balance requirement, and withdrawal amount.
balance=10000
amount=int(input("enter the withdrawal amount"))
if(amount<balance):
    print("Amount withdrawl")
    print("remainig amount:",balance-amount)
else:
    print("insufficient balance")