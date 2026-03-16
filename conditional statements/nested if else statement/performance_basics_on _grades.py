#Write a Python program that accepts a student’s percentage and classifies the performance as  excellent, very good, good, average, or poor.
per=int(input("Enter your percentage:"))
if(per>=95):
    print("Excellent")
elif(per<95 and per>=90):
    print("Very Good")
elif(per<90 and per>=80):
    print("Good")
elif(per<80 and per>=60):
    print("Average")
else:
    print("poor")