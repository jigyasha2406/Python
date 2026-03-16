#Write a program using elif to classify a person’s age group: Child, Teen, Adult, or Senior.
age=int(input("Enter your age"))
if (age<18):
    print("Child")
elif(age>=18 and age<=25):
    print("Teen")
elif(age>25 and age<50):
    print("Adult")
else:
    print("Senior")
