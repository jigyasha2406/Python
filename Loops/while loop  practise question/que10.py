#10. Write a program to remove all zeros from a number using a while loop.
new=0
place=1
n=10804
while(n>0):
    digit=n%10
    if digit!=0:
        new=new+digit*place
        place*=10
    n//=10
print(new)


