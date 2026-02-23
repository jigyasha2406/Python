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


n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if (j==0 or j==2*i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")    