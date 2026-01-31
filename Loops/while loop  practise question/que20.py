#20. Write a program to check whether a number is prime using a while loop.
n=7
fact=0
i=1
while (i<=n):
    if n%i==0:
        fact+=1
    i+=1
if fact==2:
    print("prime")
else:
    print("not prime")
