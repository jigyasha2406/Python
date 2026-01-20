#30.Write a Python program that checks whether a student qualifies for a scholarship,considering marks, family income, and category.
marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))
category = input("Enter category (GEN/OBC/SC/ST): ")

if marks >= 75:
    if income <= 250000:
        print("Eligible for Scholarship")
    else:
        if category == "SC" or category == "ST":
            print("Eligible for Scholarship")
        else:
            print("Not Eligible: Income too high")
else:
    print("Not Eligible: Marks too low")
