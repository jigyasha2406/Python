#Write a function that takes two numbers as input and returns their sum.
def sum(a,b):
    return a+b
a=int(input("enter first number"))
b=int(input("enter the second number"))
print(sum(a,b))

#Write a function that takes a number and returns its square.
def square(a):
    return a**2
a=int(input("enter a number"))
print(square(a))

#Write a function that takes a number and returns its cube.
def cube(a):
    return a**3
a=int(input("enter a number"))
print(cube(a))
  
#Write a function that takes a number and returns whether it is even or odd.
def even_odd(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
a=int(input("enter a number"))
print(even_odd(a))

#Write a function that takes a number and returns its factorial.
def fact(a):
    fact=1
    i=1
    while i<=a:
        fact*=i
        i+=1
    return fact
a=int(input("enter a number"))
print(fact(a))

#Write a function that takes two numbers and returns the larger number.
def lar(a,b):
    if (a>b):
        return a
    else:
        return b
a=int(input("enter a number"))
b=int(input("enter the second number"))
print(lar(a,b))

#Write a function that takes three numbers and returns the smallest number.
def three(a,b,c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    else:

        
        return c
a=int(input("enter a number"))
b=int(input("enter the second number"))
c=int(input("enter the second number"))
print(three(a,b,c))

#Write a function that takes a number and returns the reverse of the number.
def rev(num):
    rev=0
    while num>0:
        di=num%10
        rev=rev*10+di
        num//=10
    return rev
print(rev(1234))
    
#Write a function that takes a number and returns the sum of its digits.
def sum(num):
    sum=0
    while num>0:
        di=num%10
        sum+=di
        num//=10
    return sum
print(sum(23))

#10 Write a function that takes a number and returns whether it is a palindrome or not.
def palin(a):
    temp=a
    rev=0
    while a>0:
        di=a%10
        rev=rev*10+di
        a//=10
    if rev==temp:
        return "palindrome"
    else:
        return "not palindrome"
print(palin(121))

#Write a function that takes a number and returns the count of digits in the number.
def count(n):
    count=0
    while n>0:
        count+=1
        n//=10
    return count
print(count(1234))

#Write a function that takes a number and returns whether it is a prime number or not.
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(prime(2))   

li=[1,2,3,4,5,6]

#Write a function that takes two numbers and returns their product.
def prod(a,b):
    return a*b
print(prod(10,2))

#Write a function that takes two numbers and returns the remainder when the first number is divided by the second.
def mod(a,b):
    return a%b
print(mod(5,2))

#Write a function that takes a number and returns the sum of numbers from 1 to that number.
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(sum(3))

#Write a function that takes a number and returns the multiplication table of that number.
def mul(n):
    for i in range(1,11):
        print(n*i)
print(mul(5))

#Write a function that takes two numbers and returns the power of the first number raised to thesecond number.
def power(a,b):
    return a**b
print(power(2,3))

#18 Write a function that takes a number and returns the last digit of the number.
def last(n):
    return n%10
print(last(45349))

#19 Write a function that takes a number and returns the first digit of the number.




#20 Write a function that takes two numbers and returns the absolute difference between them.
def abs(a, b):
    if a > b:
        return a - b
    else:
        return b - a
print(abs(6, 10))
