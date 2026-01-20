#Write a Python program that checks whether a person is eligible for a loan, based on conditions such as minimum age and minimum monthly income.
age=int(input("enter your age"))
monthy_income=int(input("Enter your monthly income"))
if(age>=25):
    if(monthy_income>=25000):
        print("loan granted")
else:
    print("loan denied")
        

