#5. Write a program to check whether a number is a palindrome using a while loop.
n=121
a=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
#print(rev)
if rev==a:
    print("palindrome")
else:
    print("not")
