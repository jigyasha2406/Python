#Write a program using nested if to check whether a number is divisible by 5, and if yes, check whether it is also 
# divisible by 10.
num = int(input("Enter a number: "))
if num % 5 == 0:
    if num % 10 == 0:
        print("The number is divisible by both 5 and 10.")
    else:
        print("The number is divisible by 5 but not by 10.")
else:
    print("The number is not divisible by 5.")
