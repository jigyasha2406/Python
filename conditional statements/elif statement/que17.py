#Write a program using elif to check traffic light action based on color input.
color=input("Enter the colour of the light:")
if(color=="red"):
    print("Stop")
elif(color=="yellow"):
    print("Wait")
else:
    print("Go")