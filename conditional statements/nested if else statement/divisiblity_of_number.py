#Write a Python program that checks whether a number is divisible by 2, 3, or 5, and prints exactly which condition(s) the number satisfies.
num=int(input("enter a number:"))
if(num%2==0):
    print("the number is divisible by 2")
elif(num%3==0):
        print("the number is divisible by 3")
elif(num%5==0):
            print("the number is divisible by 5")
else:
        print("the number is not divisible by 2,3,5")