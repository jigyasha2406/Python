#Write a program using elif to check whether a given day number (1–7) corresponds to Monday–Sunday.
num=int(input("Enter a number between 1-7"))
if(num==1):
    print("monday")
elif(num==2):
    print("tuesday")
elif(num==3):
    print("wednesday")
elif(num==4):
    print("thrusday")
elif(num==5):
    print("friday")
elif(num==6):
    print("satuarday")
elif(num==7):
    print("sunday")
else:
    print("enter a valid number")
