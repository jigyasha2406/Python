#Write a Python program that accepts a year as input and checks whether it is a valid leap year using all leap year rules (divisible by 4, not divisible by 100 unless divisible by 400).
year=int(input("Enter a year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("Its a leap year")
else:
    print("Its not a leap year")