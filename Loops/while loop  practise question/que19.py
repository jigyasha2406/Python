#19. Write a program to find the GCD of two numbers using a while loop.
a=9
b=12
while b!=0:
    a,b=b,a%b
print(a)