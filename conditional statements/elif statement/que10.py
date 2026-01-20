#Write a program using elif to convert a numeric month value (1–12) into the month name.
month_num = int(input("Enter a month number (1-12): "))

if month_num == 1:
    print("January")
elif month_num == 2:
    print("February")
elif month_num == 3:
    print("March")
elif month_num == 4:
    print("April")
elif month_num == 5:
    print("May")
elif month_num == 6:
    print("June")
elif month_num == 7:
    print("July")
elif month_num == 8:
    print("August")
elif month_num == 9:
    print("September")
elif month_num == 10:
    print("October")
elif month_num == 11:
    print("November")
elif month_num == 12:
    print("December")
else:
    print("Invalid month number! Please enter 1-12.")
