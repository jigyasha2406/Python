#Write a program using elif to find the largest among three numbers.
a=int(input("Enter a number:"))
b=int(input("Enter second number:"))
c=int(input("enter third number:"))
if (a>=b and a>=c):
    print("A is greater")
elif(b>=a and b>=c):
    print("B is greater")
else:
    print("c is greater")