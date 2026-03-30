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
        