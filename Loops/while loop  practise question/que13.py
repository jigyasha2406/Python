#13. Write a program to calculate the sum of even digits and sum of odd digits separatelyusing a while loop.
even_sum=0
odd_sum=0
n=234567
while n>0:
    digit=n%10
    if digit%2==0:
        even_sum+=digit
    else:
        odd_sum+=digit
    n//=10
print(even_sum)
print(odd_sum)


