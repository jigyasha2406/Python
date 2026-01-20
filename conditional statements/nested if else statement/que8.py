#Write a Python program that checks whether a given password is valid by verifying conditions such as minimum length and presence of required characters.

password=input("Create your password")
spe="@#&"
if len(password)<8:
    if(spe not in password):
        print("invalid")
else:
    print("valid")