#20. Write a program to check whether a number is prime using a while loop.
n = 9
i = 2

while i < n:
    if n % i == 0:
        print("Not a prime number")
        break
    i += 1
else:
    print("Prime number")
