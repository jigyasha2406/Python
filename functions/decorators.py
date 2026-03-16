#Write a decorator that prints 'Function started' before execution and 'Function ended' after execution of any function.
def add_func(func):
    def wrapper():
        print("function started")
        func()
        print("function ended")
    return wrapper
@add_func
def greet():
    print("hello")
greet()

#Create a decorator that measures and prints the execution time of a function.
import time
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("execution time",end-start)
    return wrapper
@timer
def show():
    for i in range(1000000):
        pass
show()
    
#Write a decorator that checks whether the input number to a function is positive; if not, it should print an error message.
def add_func(func):
    def wrapper(num):
        if num>0:
            return func(num)
        else:
            return "ERROR"
    return wrapper
@add_func
def input(num):
    return num
print(input(-10))

#Create a decorator that logs the arguments passed to a function before calling it.
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

#Write a decorator that allows a function to be executed only once; on subsequent calls it should print 'Function alreadyxecuted'.
def func1(func):
    call=False
    def wrapper():
        nonlocal call
      
        if not call:
            func()
            call=True
        else:
            print("function already run")
    return wrapper
@func1
def show():
    print("function is runnung")
show()
show()



