#
#high oder function-into the high order function we basically pass another function as an argument.

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

#Write a function calculate that takes another function and a number as arguments and applies that function to the number.
def calculate(func,num):
    return func(num)
def square(x):
    return x*x
def cube(x):
    return x*x*x
print(calculate(square,5))
print(calculate(cube,5))

#Create a function operation that accepts two numbers and a function (like add, multiply) and returns the result after applying the function.
def number(func,num1,num2):
    return func(num1, num2)
def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
print(number(add,5,6))
print(number(multiply,5,6))

#Write a function power_generator that returns another function which calculates the cube of a number.
def power_generator(func,num):
    return func(num)
def cube(x):
    return x*x*x
print((power_generator(cube,2)))
    
#Create a function apply_twice that takes a function and a number, and applies the function two times on the number.
def apply_twice(func,num):
    return func(func(num))
def square(x):
    return x*x
print(apply_twice(square,2))

#Write a function choose_function that takes a string argument ('double' or 'triple') and returns corresponding function to multiply a number.

def choose_function(name):
    if name=="double":
        def double(n):
            return n*2
        return double
    elif name=="triple":
        def triple(n):
            return n*3
        return triple
f1=choose_function("double")
f2=choose_function("triple")
print(f1(5))
print(f2(10))


        
    