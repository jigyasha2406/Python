#11. Write a program to count how many even and odd digits are present in a number using a while loop.
even=0
odd=0
n=2468
while n>0:
    digit=n%10
    if digit%2==0:
        even+=1
    else:
        odd+=1
    n//=10
print(even)
print(odd)

