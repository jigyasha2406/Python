#Write a program using elif to check whether a number is divisible by 2, 3, 5, or none of them.
num=int(input("Enter a numbee"))
if(num%2==0):
    print("The number id divisible  by 2")
elif(num%3==0):
    print("the number is divisible by 3")
elif(num%5==0):
    print("the number is divisible by 5")
else:
    print("Not divisible by 2,3,5")
