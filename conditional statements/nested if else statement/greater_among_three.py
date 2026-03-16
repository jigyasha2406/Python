#Write a program using nested if to find the greatest among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Greatest number is:", a)
    else:
        print("Greatest number is:", c)
else:
    if b >= c:
        print("Greatest number is:", b)
    else:
        print("Greatest number is:", c)
