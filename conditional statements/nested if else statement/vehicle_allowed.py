#Write a Python program that determines whether a vehicle is allowed on the road,based on fuel type and government rules.
fuel = input("Enter fuel type (petrol/diesel): ")
age = int(input("Enter vehicle age: "))

if fuel == "petrol" and age <= 15:
    print("Vehicle allowed")
elif fuel == "diesel" and age <= 10:
    print("Vehicle allowed")
else:
    print("Vehicle not allowed")
