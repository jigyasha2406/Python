#3. Write a program to count how many digits are in a given number using a while loop.
count=0
n=6789
while n>0:
    count+=1
    n//=10
print(count)