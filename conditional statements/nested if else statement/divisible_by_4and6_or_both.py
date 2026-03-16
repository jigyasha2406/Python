#Write a Python program that checks whether a number is divisible by 4 or divisible by 6, but not divisible by both at the same time.

num = int(input("Enter a number: "))

if (num % 4 == 0 or num % 6 == 0):
    if (num % 4 == 0 and num % 6 == 0):
        print("Not satisfying (divisible by both 4 and 6)")
    else:
        print("Satisfying the condition (divisible by 4 or 6, but not both)")
else:
    print("Not satisfying")

        