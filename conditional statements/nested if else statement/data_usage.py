#Write a Python program that checks a user’s internet data usage and categorizes it as low usage, medium usage, or high usage.
data_usage=float(input("Enter your internet usage in GB:"))
if(data_usage<5):
    print("Low usage")
elif data_usage<30:
    print("Medium usage")
else:
    print("High Usage")