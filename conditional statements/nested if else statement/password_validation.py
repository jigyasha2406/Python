password=input("Create your password")
spe="@#&"
num="1234567890"
if len(password)<8:
    if(spe not in password):
        if(num not in password):
             print("invalid")
       
else:
    print("valid")