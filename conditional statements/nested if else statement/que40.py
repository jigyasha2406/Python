#Write a program using nested if to check whether a person is eligible tovote, and if eligible, check whether they are a first-time voter.
age = int(input("Enter your age: "))
first_time = input("Are you a first-time voter? (yes/no): ")
if age >= 18:
    if first_time == "yes":
         print("You are eligible to vote and you are a first-time voter.")
    else:
        print("You are eligible to vote but not a first-time voter.")
else:
    print("You are not eligible to vote.")
