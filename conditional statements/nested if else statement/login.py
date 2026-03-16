#26.Write a Python program that simulates a login system, first checking whether the username exists and then checking whether the password is correct.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "jigyasha":
    if password == "12345":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Username does not exist")
