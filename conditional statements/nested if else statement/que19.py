#Write a Python program that determines the tax slab of a person based on their annual income.
income=int(input("Enter your income:"))
if(income<=250000):
    print("No Tax")
elif(income<=500000):
    print("5% Tax")
elif(income<=1000000):
    print("20% Tax")
else:
    print("30% tax")