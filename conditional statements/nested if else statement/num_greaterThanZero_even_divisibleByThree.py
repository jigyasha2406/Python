#Write a Python program that takes an integer as input and checks whether thenumber is greater than zero, even, and divisible by 3. Print an appropriate message depending on whether all conditions are satisfied.
num=int(input("Enter a number"))
if(num>0):
    if(num%2==0):
        if(num%3==0):
            print("the entered number is positive,even,divisble by 3")
    else:
        print("Not fulfilled any condition")
    
            
    