new=0
n=102
while n>0:
    digit=n%10
    if digit!=0:
        new=new+digit*10
        n=n//10
print(new)
    