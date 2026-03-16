#Write a Python program that accepts marks of three subjects and checks whetherthe student has passed in all subjects, assuming the pass mark is 40 in each subject.
english=int(input("Enter your english marks"))
maths=int(input("Enter your maths marks"))
science=int(input("Enter your science marks "))
if(english>=40):
    if(maths>=40):
        if(science>=40):
            print("Pass")
else:
    print("Fail")
    