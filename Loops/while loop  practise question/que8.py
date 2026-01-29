#8. Write a program to find the smallest digit in a number using a while loop.
small=9
n=7853421
while n>0:
    digit=n%10
    if digit<small:
        small=digit
    n//=10
print(small)
