#7. Write a program to find the largest digit in a number using a while loop.
n=123589
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n//=10
print(largest)