#2. Write a program to find the sum of digits of a number using a while loop.
sum=0
n=12345
while n>0:
    di=n%10
    sum+=di
    n=n//10
print(sum)