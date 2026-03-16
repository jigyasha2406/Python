#Write a Python program that determines a student’s exam result category,considering pass marks and a small grace-marks rule.
marks = int(input("Enter obtained marks: "))

if marks >= 0 and marks <= 100:
    if marks >= 40:
        print("Result: Pass")
    else:
        if marks >= 35:
            print("Result: Pass by Grace")
        else:
            print("Result: Fail")
else:
    print("Invalid marks")
