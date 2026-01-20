#Write a program using nested if to check whether a student has passed orfailed, and if passed, assign a grade based on marks.
status="pass"
marks=int(input("enter your marks"))
if(status=="pass"):
  if marks>=40:
    print("pass")
    print("grade=A")
  else:
    print("fail")
    print("grade=b")