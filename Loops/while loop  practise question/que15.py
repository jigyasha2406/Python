#15. Write a program to check whether a number is a perfect number using a while loop.
n=6
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("Perfect Number")
else:
    print("Not perfect")
















