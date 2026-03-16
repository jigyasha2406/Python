#Write a program using elif to calculate electricity bill based on unit ranges.
units = int(input("Enter electricity units: "))

if units <= 100:
    print("Bill Amount: ₹100")
elif units <= 200:
    print("Bill Amount: ₹200")
elif units <= 300:
    print("Bill Amount: ₹300")
else:
    print("Bill Amount: ₹500")
