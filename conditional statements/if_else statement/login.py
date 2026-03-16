#Write a program using if-else to check whether a user is allowed to
#access a page (logged_in is True and role is "admin").

role=input("Enter your role:")
logged_in=True
if(role=="admin" and logged_in==True):
    print("Access granted")
else:
    print("Access denied")

