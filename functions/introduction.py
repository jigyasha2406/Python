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

# high order function ,map ,filter,lamda.

#high oder function-into the high order function we basically pass another function as an argument.
def func1(fun):
    print("this is the func 1")
    fun()
def hello():
    print("hello")
func1(hello)
 #example 
def high_order(simple):
    simple()
def simple():
    print("simple")
def say_hello():
    print("this is the hello from hello function")
high_order(say_hello)
high_order(simple)

#CREATE A high order function that filter outs the even numbers from the list
li=[1,2,3,4,5,6]
def high_order(func,li):
    li1=[]
    for num in li:
        if is_even(num):
            li1.append(num)
    return li1
def is_even(n):
    if n%2==0:
        return True
    return False   
#li=[1,2,3,4,5,6]
print(high_order(is_even,li))    

#filter out the negative number from a list
li=[1,2,-1,-3,4]
def high_order(func,li):
    li1=[]
    for num in li:
        if is_negative(num):
            li1.append(num)
    return li1
def is_negative(num):
    if num<0:
        return True
    return False
print(high_order(is_negative,li))

# filter out prime numbers
li=[1,2,3,7,8]
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def high_order(func,li):
    li1=[]
    for n in li:
        if prime(n):
            li1.append(n)
    return li1
print(high_order(prime,li))

# filter method is ahigh order function which is used to filter out the iterables in which the first argumnet be the function name and second would be the iterable#
#syntax->filter(func_name,iterable)
# it return by default a object and we can convert the filtered object into the list or tuple
def is_even(n):
    if n%2==0:
        return True
    return False  
li=[1,2,3,4,5]
print(list(filter(is_even,li)))

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
li=[1,2,3,4]
print(list(filter(prime,li)))

# map function-

#lamda,decorators,map,high order function
#map-map is a python bulti-in function which is used to apply a function to the every element of the iterable
#lamda-a lamdais a anaoynums function which is used to perform smal task 

# map function is also a high order function which map all the values of a iterable with a function
#syntax-map(func,iterable)
#square of each element in the list
li=[1,2,3,4]
def sq(x):
    return x**2
print(list(map(sq,li)))

#lamda function-is a anaoymus and the on eliner function which is used generally into the higher order function or it is used for one time use
# lamda is inatialized with the lamda keyword
#syntax-lamda parameter:expression
li=[1,2,3,4]
print(list(map(lambda x:x**2,li)))

#CHECK WHETHER A NUMBER IS EVEN OR ODD
f1=lambda n :"even" if n%2==0 else "odd"
print(f1(10))

#decorators-is a high order function which  make changes or modifies the existing function without changing the original code
# decorater is a high order function which takes another function as an argument to enhance or add the functionality to the exixting function without changing the code of that function .
def shopkeeper(mobile):
    def person():
        print("chamkeele panni")
        mobile()
        print("name slip")
    return person
@shopkeeper
def mobile():
    print("ye raha mera phone")
mobile()

def add_func(func):
    def wrapper():
        print("welcome user")
        func()
    return wrapper
def add_func1(func):
    def wrapper():
        print("decorator 2 is running")
        func()
    return wrapper
@add_func
@add_func1
def loginn():
    print("user logged in")
loginn()

def add_func(func):
    def wrapper():
        result=func()+5
        return result
    return wrapper
    
@add_func
def func1():
    return 10
func1()

def add_value(fun):
    def wrapper():
        result=fun()+5
        return result
    return wrapper

@add_value
def func1():
    return 10
print(func1())

def func1(func):
    def wrapper(a,b):
        print(a)
        print(b)
        result=func(a,b)
        return result
    return wrapper
@func1 
def add_num(a,b):
    print(a+b)
add_num(10,20)

# write a program to check whether the input is positive or not and add the functionality to the function of the power
def add_func(func):
    def wrapper(a):
        if a>0:
            return func(a)
        else:
            return "number is not positive"
    return wrapper
@add_func
def power(a): 
    return a**2
print(power(2))
 

 


