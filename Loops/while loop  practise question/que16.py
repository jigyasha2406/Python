#16. Write a program to print the Fibonacci series up to N terms using a while loop.
n = 8

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
