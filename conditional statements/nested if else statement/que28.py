#28.Write a Python program that checks whether a student is eligible for admission,based on academic marks and an entrance test score.
marks = int(input("Enter academic marks: "))
entrance = int(input("Enter entrance test score: "))
if marks >= 60:
    if entrance >= 50:
        print("Eligible for Admission")
    else:
        print("Not eligible: Entrance score too low")
else:
    print("Not eligible: Academic marks too low")
