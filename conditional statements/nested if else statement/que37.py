#Write a program using nested if to check whether a number is positive,negative, or zero, and if positive, also check whether it is even or odd.
num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    if num < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")
