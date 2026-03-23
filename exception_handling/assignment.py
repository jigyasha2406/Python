#Write a function that takes two numbers and performs division. Use else block to print the result if no error occurs and finally block to print Execution completed.
try:
    a=10
    b=5
    c=a//b
except:
    print("something happend")
else:
    print(c)

#Create a function that converts a given input into integer. Use else block to print theconverted value and finally block to print Conversion attempt finished.
try:
    a="10"
    b=int(a)
except:
    print("something happend")
else:
    print(b)
finally:
    print("execution completed")

#Implement a function that calculates square of a number after converting input to float. Use else block to return the square and finally block to display Process done.
def square(a):
    try:
        b=float(a)
    except:
        print("something went wrong")
    else:
        return b**2
    finally:
        print("process done")
print(square(3))

#Write a function that performs floor division of two numbers. Use else block to print quotient and finally block to print Function executed.
def floor(a,b):
    try:
        c=a//b
    except:
        print("somethig happend")
    else:
        print(c)
    finally:
        print("function executed")
floor(10,2)

#Create a function that finds reciprocal of a number. Use else block to print the reciprocal and finally block to print End of operation.    
def reciprocal(a):
    try:
        c=1/a
    except ZeroDivisionError as e:
        print("something went wrong",e)
    else:
        print(c)
    finally:
        print("end of the operation")
reciprocal(2)
    
#Implement a function that multiplies two inputs after converting them into integers. Use else block to print product and finally block to print Multiplication tried.
def multiplication(a,b):
    a=int(a)
    b=int(b)
    try:
        c=a*b
    except:
        print("something is happend")
    finally:
        print("Multiplication tried")

#Write a function that calculates percentage using marks and total marks. Use else 2block to print percentage and finally block to print Calculation finished.
def percentage(marks,total_marks):
    try:
        result=marks/total_marks*100
    except ZeroDivisionError:
        print("somtehing went wrong")
    else:
        print(result)
    finally:
        print("calculation finished")
percentage(80,120)
    
#Create a function that converts string input into float and prints half of it. Use else blockfor output and finally block for completion message.
def half(name):
    s=float(name)
    try:
        result=s/2
    except:
        print("something happend")
    else:
        print(result)
    finally:
        print("task completed")
half("12")

#Implement a function that performs modulus operation. Use else block to print remainder and finally block to print Modulus attempt done.
def modulus(a, b):
    try:
        result = a % b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print( result)
    finally:
        print("Modulus attempt done")

#Write a function that calculates power of a number. Use else block to print result andfinally block to print Power function executed.

def power(a, b):
    try:
        result = a ** b
    except Exception as e:
        print("Error:", e)
    else:
        print( result)
    finally:
        print("Power function executed")

#Create a function that returns absolute value after converting input safely. Use else block to print absolute value and finally block to print Absolute check completed.
def absolute_value(x):
    try:
        num = float(x)
    except ValueError:
        print("Invalid input")
    else:
        print(abs(num))
    finally:
        print("Absolute check completed")

#Implement a function that divides three numbers step by step. Use else block to printfinal result and finally block to print Division process ended.

def divide_three(a, b, c):
    try:
        first= a / b
        second= step1 / c
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print("Error:", e)
    else:
        print(second)
    finally:
        print("Division process ended")

#Write a function that converts input into integer and prints its double. Use else block for result and finally block for closing message.
def double_value(x):
    try:
        num = int(x) 
    except ValueError:
        print("Invalid input")
    else:
        print( num * 2)
    finally:
        print("Operation completed")

#Create a function that subtracts two numbers after safe conversion. Use else block to print difference and finally block to print Subtraction attempt finished.
def subtract(a, b):
    try:
        num1 = float(a)
        num2 = float(b)
        result = num1 - num2
    except ValueError:
        print("Invalid input")
    else:
        print(result)
    finally:
        print("Subtraction attempt finished")
    
#Implement a function that calculates average of two numbers. Use else block to printaverage and finally block to print Average calculation done.
def average(a, b):
    try:
        num1 = float(a)
        num2 = float(b)
        avg = (num1 + num2) / 2
    except ValueError:
        print("Invalid input")
    else:
        print( avg)
    finally:
        print("Average calculation done")

#Write a function that calculates square root after converting input to float. Use else block to print result and finally block to print Square root operation finished.
def square_root(x):
    try:
        num = float(x)
        result = num ** 0.5
    except:
        print("Invalid input")
    else:
        print( result)
    finally:
        print("Square root operation finished")

#def simple_interest(p, r, t):
    try:
        p = float(p)
        r = float(r)
        t = float(t)
        si = (p * r * t) / 100
    except:
        print("Invalid input")
    else:
        print("Simple Interest:", si)
    finally:
        print("Interest calculation attempt done")

# Create a function that performs simple interest calculation. Use else block to print interest and finally block to print Interest calculation attempt done.
def simple_interest(p, r, t):
    try:
        p = float(p)
        r = float(r)
        t = float(t)
        si = (p * r * t) / 100
    except:
        print("Invalid input")
    else:
        print(si)
    finally:
        print("Interest calculation attempt done")

#Implement a function that divides a number by itself after safe conversion. Use else block to print result and finally block to print Self division completed.
def self_division(x):
    try:
        num = float(x)
        result = num / num
    except:
        print("Invalid input or division by zero")
    else:
        print(result)
    finally:
        print("Self division completed")

#Write a function that finds remainder after safe integer conversion of inputs. Use else block to print remainder and finally block to print Remainder operation finished.
def remainder(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        result = num1 % num2
    except:
        print("Invalid input or division by zero")
    else:
        print(result)
    finally:
        print("Remainder operation finished")
#Create a function that performs multiplication of three numbers. Use else block to print product and finally block to print Multiplication process completed.
def multiply(a, b, c):
    try:
        num1 = float(a)
        num2 = float(b)
        num3 = float(c)
        result = num1 * num2 * num3
    except:
        print("Invalid input")
    else:
        print(result)
    finally:
        print("Multiplication process completed")



