#Write a program using nested if to check whether a person is eligible for ajob based on age, and if eligible, check whether they have the required qualification.
age = int(input("Enter your age: "))
qualification = input("Do you have the required qualification? (yes/no): ")
if age >= 18:
     if qualification == "yes":
           print("You are eligible for the job.")
     else:
        print("You are not eligible due to lack of qualification.")
else:
      print("You are not eligible due to age.")
          