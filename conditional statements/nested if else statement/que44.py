#Write a program using nested if to check whether a number is greater than 50, and if yes, check whether it is also greater than 100.
num=int(input("Enter the number"))
if(num>50):
    if(num>100):
        print("the number is greater than both 50 ans 100")
    else:
        print("the number is greater than 50")
else:
    print("the number is not greater than 50")