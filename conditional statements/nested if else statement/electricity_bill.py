#Write a Python program that calculates an electricity bill using slab-wise unit charges and prints the total bill amount.
unit=int(input("Enter the units:"))
if(unit<=100):
    print("total_bill",unit*5)
elif(unit>100 and unit<=200):
    print("total_bill",unit*7)
elif(unit>200 and unit<=300):
    print("Total_bill",unit*10)
else:
    print("Total_bill:",unit*15)