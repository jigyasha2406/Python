#Write a Python program that checks whether a string is not empty and also has a length greater than 8 characters.
str=input("Enter the string:")
if len(str)!=" ":
    if len(str)>8:
        print("valid")
    else:
        print("Invalid")

