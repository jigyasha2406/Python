#Write a program using elif to determine the season based on month number.
month=int(input("Enter month number(1-12): "))
if month == 12 or month == 1 or month == 2:
    print("Season:winter")
elif month == 3 or month == 4 or month==5:
    print("Season:summer")
elif month==6 or month==7 or month==8:
    print("Season:monsoon")
elif month==9 or month==10 or month==11:
    print("season:Autumn")
else:
    print("Invalid month number")