#Write a Python program that takes a number and determines whether it is positive even, positive odd, negative even, negative odd, or zero.
num=int(input("Enter a number"))
if(num>0):
    if(num%2==0):
        print("Positive even")
    else:
        print("Positive odd")
if (num<0):
    if(num%2==0):
        print("Negative even")
    else:
        print("negative odd")
