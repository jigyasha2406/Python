#print("hello world")
#a= input("enter you first name:")
#b=input("enter you second name:")
#print("first_name:",a)
#print("second_name:",b)

#print("hello",a,b)
#
#input statement give string by 
age=int(input("enter your age:"))
name=input("enter your name:")
loc=input("enter your location: ")
branch=input("Enter your branch:")

print(f"I'm {name}.My age is {age}.")
print("My name is {}.My age is {}.I live in {}.I'm from branch {}".format(name,age,loc,branch))

for i in range(1,4+1):
    for j in range(1,4+1):
        print("*",end=" ")
    print()

