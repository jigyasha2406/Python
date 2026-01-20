#Write a program to check if a person can vote (age ≥ 18 and citizen is True) using if 

age=int(input("Enter your age:"))
citizen=input("are you a citizen:")
if(age>=18 and citizen=="yes"):
    print("You are eligible to vote ")