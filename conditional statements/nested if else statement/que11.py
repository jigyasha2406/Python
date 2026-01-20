#Write a Python program that checks whether a given temperature lies within a comfortable range, where both lower and upper limits are predefined.
upper=28
lower=13
temp=int(input("Enter the temperature"))
if(temp>=13):
    if(temp<=23):
        print("Lies in the confortable range")
    else:
        print("Not lies in the confortable range") 
       