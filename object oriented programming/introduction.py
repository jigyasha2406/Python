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
#to access the property of the object we use "." followed by object name
print(obj.college)

