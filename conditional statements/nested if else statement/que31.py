#Write a Python program that determines whether an employee is eligible for a bonus, based on performance rating and years of service.
rating = int(input("Enter performance rating (1-5): "))
years = int(input("Enter years of service: "))
if rating >= 4:
    if years >= 2:
        print("Eligible for Bonus")
    else:
        print("Not Eligible: Insufficient years of service")
else:
    print("Not Eligible: Performance rating too low")
