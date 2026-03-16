#Write a program using elif to check whether a number is one-digit, two-digit,three-digit, or more.
num=int(input("enter the number"))
if -9<=num<=9:
    print("one digit number")
elif -99<=num<=99:
    print("Two-digit number")
elif -999<=num<=999:
    print("Three digit number")
else:
    print("More than three digit")