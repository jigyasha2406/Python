#1. Write a program using a while loop to print all digits of a number one by one.
n=14567
while n>0:
    digit=n%10
    print(digit)
    n=n//10
