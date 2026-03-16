#Write a program using elif to check the type of input number: zero, positive even,positive odd, or negative.
num=int(input("enter a number:"))
if(num==0):
    print("you have entered zero")
elif(num>0 and num%2==0):
    print("Positive even")
elif(num>0 and num%2!=0):
    print("Positive odd")
else:
    print("Negative")

