#exceptions-exception in python are the events that occur during the excecution of a progrom that distrub its normal flow.
#error-are the general error which contians both the syntax error anf the runtime error.
#exeptions can be handle by using the try and accept block
#first the try block will run if their is any exception has occured during the execution of the try block then the except block will run .
#example:-
#try:
    #print(10/0)
#except zerodivisionerror as e:
    #print("something went wrong",e)

#syntax-
#try:
    #expression for executing the code
#except exception_error:
     #print the message why the exception is occcured
# their are basically four block in exception handling:
#try,catch,else,finally

def divide(a,b):
    #whenever any input into the function
    #then it execute the try block
    try:
        result=a/b
        return result
    #if there ia any exception into the try block 
    #then this except block will run
    except ZeroDivisionError:
        return "somrthing went wrong"
print(divide(10,0))

try:
    a="10"
    b=20
    c=a+b
    print(c)
except TypeError as e:
    print("something is hapend",e)

# else block will run when the try block ids successfully executes,it means when their is no exception is occured
try:
    a=10
    b=20
    c=a+b
    
except TypeError as e:
    print("something is hapend",e)
else:
    print(c)

#finally-finally block will always run either any exception or any error during excution of the program.
#this is basically used in the file i/o operation.
try:
    a="10"
    b=20
    c=a+b
     
except TypeError as e:
    print("something is hapend",e)
else:
    print(c)
finally:
    print("this block will always run ")



        
    


