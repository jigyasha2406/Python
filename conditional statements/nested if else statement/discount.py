#22.Write a Python program that calculates the final payable amount after applying different discount slabs based on the purchase amount.
bill=int(input("Enter the total amount of bill"))
if bill<1000:
    print("no discount")
elif bill>=1000 and bill<5000:
    print("You got 10% discout,now yout total bill:",bill-(bill*0.10))
elif bill>=5000 and bill<10000:
    print("you got 20% discount,total bill:",bill-(bill*0.20))
else:
    print("you got 30% discount,total bill:",bill-(bill*0.30))