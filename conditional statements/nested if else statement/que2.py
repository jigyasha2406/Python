#Write a Python program that takes a number as input and checks whether it lies outside the range 10 to 50 (that is, less than 10 or greater than 50).
num=int(input("Enter a number"))
if(num < 10):
    if(num>50):
        print("The number is between the range")
else:
    print("the number is not between the range")
        