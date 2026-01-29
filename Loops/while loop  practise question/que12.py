#12. Write a program to check whether a number contains a specific digit (for example, 5 using a while loop.
n=1234567
spe=5
con=False
while n>0:
    digit=n%10
    if digit==5:
        con=True
        break
    n//=10
if con:
    print("It conntains")
else:
    print("It not contains")
    
    
  