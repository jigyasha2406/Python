#6. Write a program to find the product of digits of a number using a while loop.
prod=1
n=1234
while n>0:
    digit=n%10
    prod=prod*digit
    n//=10
print(prod)