#Write a program using if-else to check whether a person can enter a club (age ≥ 21 and has ID).
age=int(input("Enter your age:"))
id=input("Do you have id?")
if(age>=18 and id=="yes"):
    print("allowed")
else:
    print("Not allowed")