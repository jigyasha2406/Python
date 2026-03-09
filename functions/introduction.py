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


    

    

