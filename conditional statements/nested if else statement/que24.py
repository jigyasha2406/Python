#24.Write a Python program that accepts a month number and prints the corresponding season (summer, rainy, or winter).
month = int(input("Enter month number (1-12): "))

if month == 3 or month == 4 or month == 5:
    print("Season: Summer")
elif month == 6 or month == 7 or month == 8 or month == 9:
    print("Season: Rainy")
elif month == 10 or month == 11 or month == 12 or month == 1 or month == 2:
    print("Season: Winter")
else:
    print("Invalid month number")
