#Write a Python program that checks whether a given character is neither a digit nor a special character, meaning it must be an alphabet.
a = input("Enter a character: ")
num = "1234567890"
spe = "!@#$%^&*_-"
a = input("Enter a character: ")
if a in num:
    print("It is a number")
else:
    if a in spe:
        print("It is a special character")
    else:
        print("It is an alphabet")


#if a not in num:
   # if a not in spe :
        #print("its a alphabet")
    #else:
        #print("its a special character or a number")
#else:
   # print("its a number")