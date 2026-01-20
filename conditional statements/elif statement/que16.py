#Write a program using elif to convert percentage into grade category.
per=int(input("Enter your percentage:"))
if(per>=95):
    print("O")
elif(per<95 and per>=90):
    print("A+")
elif(per<90 and per>=80):
    print("A")
elif(per<80 and per>=70):
    print("B")
elif(per<70 and per>=60):
    print("C")
else:
    print("D")