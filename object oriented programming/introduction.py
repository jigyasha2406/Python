#object oriented programming ia a programming paradigm based on "object" that contains data (attribute) and code(method),used to model real world entites.
#it aims to improve code reusability,structure,and maintainability through four main principle:-encapsulation,abstraction,inheritance and polymorphism.

#class(attribute)-class is the blueprint of the object or the real world entity.
#for example-car structure->wheels,stairing,side mirror 
#class is defined using the class keyword
#
class Student :
    college="IIT kanpur"
#object(instance)->object is the real world entity which have some properties
#car->blue,alloywheels
#to create the object of the class we basically use the class_name()
obj=Student()
#to access the property of the object we use "." followed by property name
print(obj.college)


class car:
    #class attribute
    manufacture="suzuki"
    #constructor
    #when the object is instantiated then this constructor method id called automatically to initialize the location memory refrence of a particular object or instance attribute
    def __init__(self,color):
        #color_name->this instance attribute
        #self->keyword is used to show the current refrence or the object 
        #this show the current object refrence
        self.color_name=color
car1=car("red")
car2=car("blue")
print(car1.color_name)




class Student:
    college="IIT"
    def __init__(self,name,branch,location):
        self.student_name=name
        self.student_branch=branch
        self.student_location=location
student1=Student("rahul","cse","jaipur")

student2=Student("jigyasha","ee","jaipur")
print(student2.student_branch)
print(student2.student_location)
print(student2.student_name)
print(student2.college)
         
#construtor - it is a method 
        
#employee managememnt system
class Employee:
    company="TCS"
    def __init__(self,emp_id,name,gender,salary):
        self.emp_id=emp_id
        self.name=name
        self.gender=gender
        self.salary=salary
    def display(self):
        print(f"Emp ID:{self.emp_id}")
        print(f"employee name:{self.name}")
        print(f"employee gender:{self.gender}")
        print(f"company:{self.company}")

emp1=Employee(123,"vishal","male",200)
emp1.display()

#create a class student which have some property like student name,location,id,branch,college
#create two student object
#and printtheir detail using the method
#write in comment the work each line
#change the valuesof the object after the creation
class Student:
    college="JECRC University"
    def __init__(self,name,location,id,branch):
        self.name=name
        self.location=location
        self.id=id
        self.branch=branch
    def display(self):
        print(f"stu_id{self.id}")
        print(f"stu_name:{self.name}")
        print(f"stu_branch:{self.branch}")
        print(f"stu_location:{self.location}")
student1=Student("anjali","jaipur",123,"CSE")
student2=Student("namrata","bhopal",124,"civil")
#student1.display()
print()
student2.display()
student1.name="jigysha"
student1.display()
