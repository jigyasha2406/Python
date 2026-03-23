#recursion is a process in which it calls or in which function calls itself until the condition is not met.
def hello(n):
    #this is the base condition
    #if the condition is true then the function call would be stopped
    if n==5:
        return
    print("hello")
    # this function call is nothing but the recursion call for the next number
    hello(n+1)
hello(1)

#num printing from 1 to 5
def func(n):
    if n==6:
        return
    print(n,end=" ")
    func(n+1)
func(1)

# print all the numbers from 10 to 1
def func(n):
    if n==0:
        return
    print(n,end=" ")
    func(n-1)
func(10)

#print all the even number from 1 to 20
def func(n):
    if n==21:
        return
    elif n%2==0:#we can use if also here
        print(n)
    func(n+1)
func(1)

#print the sum of 1 to 10:
def sum(n):
    if n==11:
        return 0
    result=n+sum(n+1)
    return result
print(sum(1))

def add(n):
    if n==1:
        return 1
    result=n+add(n-1)
    return result
print(add(5))
    

#print the sum of even number using recurssion
def sum(n):
    if n==11:
        return 0
    if n%2==0:
         result=n+sum(n+1)
         return result
print(sum(1))

def func(n):
    if n==21:
        return 0
    elif n%2==0:#we can use if also here
        result=n+func(n+1)
        return result
print(func(1))

def func1(n):
    if n<1:
        return
    if n%2==0:
        print(n)
    func1(n-1)
func1(5)

def func1(n):
    if n<1:
        return
    if n%2==0:
        print(n)
    func1(n-1)
func1(5)

#power calculate 
def power(a,b):
    if b==0:
        return 1
    return a* pow(a,b-1)
print(pow(2,3))

#sum of all even numbers
def sum(n):
    if n==10:
        return 0
    if n%2==0:
        return n+sum(n+1)
    else:
        return sum(n+1)
print(sum(1))


#print the factorial using the recursion\
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
print(factorial(5))

# print the fibonacci sequence for the nth element
def fibb(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibb(n-2) + fibb(n-1)
print(fibb(5))

# print the sequence of the fibonacci series
def fibb(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibb(n-2) + fibb(n-1)
for i in range(8):
    print(fibb(i))

#count the number of digit in a number
def count(n):
    if n==0:
        return 0
    #if n==1:
        #return 1
    return 1 + count(n//10)
print(count(1234))

# print the sum of all the digits of a number
def count(n):
    if n==0:
        return 0
    return (n%10) + count(n//10)# + count(n+1)
print(count(1234))
    
n=1234
sum=0
while(n>0):
    di=n%10
    sum+=di
    n//=10
print(sum)

#reverse the number of digit using recursiion
n=1234
rev=0
while(n>0):
    di=n%10
    rev=rev*10+di
    n//=10
print(rev)

def rev(n,r=0):
    if n==0:
        return 0
    return rev()
print(rev(1234))



li=[1,2,3,4]
