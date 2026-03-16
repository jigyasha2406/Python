#Write a Python program that accepts a person’s age and checks whether the person is eligible to vote (age ≥ 18) and not a senior citizen (age < 60).
age=int(input("enter your age "))
if(age>=18):
    if(age<60):
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
    