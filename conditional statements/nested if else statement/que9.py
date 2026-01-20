#Write a Python program that checks whether a number lies between 100 and 999 (inclusive) and is also an even number.
num=int(input("Enter a number"))
if(num>=100 and num<=999):
    if(num%2==0):
        print("The number lies between the range as well its a even number")
   
else:
    print("not in range")