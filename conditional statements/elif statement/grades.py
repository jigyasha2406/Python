#Write a program using elif to assign grades based on marks:A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).
marks=int(input("Enter your marks"))

if(marks>=90 and marks<=100):
    print("A")
elif(marks>=80 and marks<=89):
    print("B")
elif(marks>=70 and marks<=79):
    print("C")
elif(marks>=60 and marks<=69):
    print("D")
else:
    print("F")
