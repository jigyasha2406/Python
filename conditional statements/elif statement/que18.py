#Write a program using elif to classify temperature as Cold, Moderate, or Hot.
temp=int(input("Enter the temperature"))
if(temp<15):
    print("Cold")
elif(temp>15 and temp<25):
    print("Moderate")
else:
    print("Hot")