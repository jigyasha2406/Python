#fuctions-functions is a block of code which is used to perform a specific task  
# in python we define the function with the def keyword followed by the function name()
# syntax-> def function_name():
             #expression
# calling function-function_name
def hello():
    print("hello from class")
hello() # calling the function

#paremetrs-are the variable which are passed or defined at the time of the function defination.
def greeting(name):
    print(f"hello",{name})
greeting("jigyasha") 

def add(a,b):
    print(f"the sum is :{a+b}")
add(10,15)

#return keyword is used to return any value from the function 
def add(a,b):
    return a+b
sum=add(10,15)
print(sum)

# waf to check where the even or odd
def func(num):
    if num%2==0:
        return True
    return False
print(func(10))
if func(10):
    print("the number is even")
else:
    print("the number is odd")

#waf to check whether a number is prime or not
def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(prime(10))
if prime(10):
    print("number is prime")
else:
    print("number is not prime")

def is_prime(num):
    fact=0
    for i in range(1,num+1):
        if num%i==0:
            fact+=1
    if fact==2:
        return True
    else:
        return False
for i in range(2,101):
    if is_prime:
        print(i,end=" ")
if is_prime(8):
    print("prime")
else:
    print("not prime")


def print_primes():
    for num in range(2, 101):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num,end=" ")

print_primes()
# default,keyword,var_length,pass by value,pass by refrence 
# default,keyword,var_length

# default argument-is a parameter that alraedy has a value,if user does not provide any value then pyton uses that default value.

# positional argument-are the arguments which are passed on the basis of the function definition based on their parameter position.

# keyword argument- we pass value using the parameter name.
#keyword are the method of passing values to a function during a function call by explicitly specify the parameters name.
# variable length-it is used when we dont know how many arguments will be passed-*args
# variable name srguments are the arguments which are passed with the variable name
#syntax- def func_name(*arguments)
# it return tuple
def add(*args):
    print(sum(args))
add(1,2)
def details(**args):
    for key,value in args.items():
        print(f"{key}->{value}")
details(name="rahul",location="jaipur",batch="A26")
#pass by value- it is a copy of a value is passed to the function ,changes inside the function does not affect the original value
# in call by value the values are or the copied values are passed into the function as an  argument,it doesnt change the original value
# into this only immutable object are condsidered as call by value
def func(a):
    a=a+10
    print(a)
a=10
print(func(a))
print(a)
# pass by refrence-the original object is modified 
#usually happend in list,dictonaries,set
# call by refrence into this we basically pass the refrence at the time of function call,into the python it is automaticlly done when we pass any mutable object into the function
# in call by refrence the original object is change whenever we make changes from the function
def func(li):
    li.append(10)
    print(li)
li=[1,2,3,4]
func(li)
print(li)

# arguments are the value that you pass toa function when you call it
#parameters are the variables written in the function definition
def greet(name):#parameter
    print("hello!",name)
greet("jigyasha")# arguments
    
#local variable are accesible only into the function
#global variables are accesible into the function and outside the function also .
# if we want to change the value of a global variable then we use a global keyword into the function
b=20
def hello():
    global b
    b=30
    a=10
    print(a)
    print(b)
hello()

# call by value- 
