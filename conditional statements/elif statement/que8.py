#Write a program using elif to build a simple calculator for +, -, *, and /.
num1=int(input("Enter a number"))
num2=int(input("Enter secong number"))
ope=input("Select the operation +,-,*,/,//,**:")
if(ope=="+"):
    print(num1+num2)
elif(ope=="-"):
    print(num1-num2)
elif(ope=="*"):
    print(num1*num2)
elif(ope=="/"):
    print(num1/num2)
elif(ope=="//"):
    print(num1//num2)
elif(ope=="**"):
    print(num1**num2)
else:
    print("enter a valid operation")

