#Write a program using elif to check the result of a student: Distinction, First Class, Second Class, Pass, or Fail.
total_marks=int(input("Enter the marks"))
if(total_marks>400):
    print("Distinction")
elif (total_marks<=400 and total_marks>350):
    print("First class")
elif(total_marks<=350 and total_marks>300):
    print("Second class")
elif(total_marks<300 and total_marks>200):
    print("Pass")
else:
    print("Fail")
