#Write a program using if-else to check whether a year is a leap year or not.
year=int(input("Enter a year"))
if(year%4==0 and year%100!=100) or (year%400==0):
    print("the Enterd year ia a leap year")
else:
    print("Not a leap year")