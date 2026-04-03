#inheritance is the property of object oriented programming or one of the four pillar which makes parent class property accessible to child class.
# single inheritence-in single level inheritance their is only one parent and one child.

# multiple inheritance
# multi level
# hybrid
# ex= property of the father is inherited to child
# 
#in heritance basically all the attribute and the methods are accesible to the child class
class father:#this is the parent class
    highway_property="property"
    def father_property(self):
        print("this is access to all the property of the father")
#here we have inherited from the father class to the child
class child(father):
    pass
child=child()
print(child)
#here we are accessing the father property
print(child.highway_property)

class employee:
    company="TCS"
    def __init__(self,name,salary,gender):

        self.name=name
        self.salary=salary
        self.gender=gender
class developer(employee):
    def __init__(self,name,salary,gender,department):
        #using the super keyword we inatialize the parent instance attribute
        super().__init__(name,salary,gender)
        self.department=department
    
obj=developer("shyam",20000,"male","software engineer")
print(obj.salary)
print(obj.company)
print(obj.department)

#multi-level inheritance- in multilevel inheritance basically their is more than one level of inheritance is given.
# eg- grandfather->father->child

class grandFather:
    grandfather_prop=("Grandfathers property")
class Father(grandFather):
    Father_prop="Fathers property"
class child(Father):
    child_prop="childs property"
obj=child()
print(obj.grandfather_prop)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employee(person):
    def __init__(self,name,age,dep):
        super().__init__(name,age)
        self.dep=dep
class manager(employee):
    def __init__(self,name,age,dep,team_size):
        super().__init__(name,age,dep)
        self.team_size=team_size
    def details(self):
        print("name:",self.name)
        print("age:",self.age)
        print("dep:",self.dep)
        print("team_size:",self.team_size)
obj=manager("rahul",24,"ML",50)
obj.details()


#multiple inheritance-in multiple inheritance basically their is more than one parent of the derived class or the child class
# class a , class b ,class(a,b)
class cngCar:
    cng_prop="this call will be run on cng"
    def __init__(self,cylinder):
        self.cylinder=cylinder
    def display(self): 
        print("thid is a cng car")
class petrolCar:
    petrol_prop="this car will be run on petrol"
    def __init__(self,tank):
        self.tank=tank
    def display(self):
        print("petrol car")
class HybridCar(cngCar,petrolCar):
    def __init__(self,tank,cylinder):
        cngCar.__init__(self,cylinder)
        petrolCar.__init__(self,tank)
    hybrid_pro="this car will run on both petrol and cng"
    def dispaly(self):
        print("this is a hybrid car")
obj=HybridCar(20,50)
print(obj.tank)
print(obj.cylinder)
#MRO-method resolution order->it defines or decide how the method of the different class would run.
#A-display
#b-dispaly
#c(A,B)
#c-obj->obj.display->here class A display method is called
#class -c,class A,class B

#hybrid inheritance-it is the combination of both multilevel and multiple inhritance.
class Vehicle:
    pass
class car:
    pass
class cngCar(car):
    cng_prop="this call will be run on cng"
    def __init__(self,cylinder):
        self.cylinder=cylinder
    def display(self): 
        print("thid is a cng car")
class petrolCar(car):
    petrol_prop="this car will be run on petrol"
    def __init__(self,tank):
        self.tank=tank
    def display(self):
        print("petrol car")
class HybridCar(cngCar,petrolCar):
    def __init__(self,tank,cylinder):
        cngCar.__init__(self,cylinder)
        petrolCar.__init__(self,tank)
    hybrid_pro="this car will run on both petrol and cng"
    def dispaly(self):
        print("this is a hybrid car")
obj=HybridCar(20,50)
print(obj.tank)
print(obj.cylinder)

#class method-class mehod is used to change to update the class attribute using the classmethod decorator
#into the method thr first parameter is cls
class student:
    college="IIT"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_college(cls,new_college):
        cls.college=new_college
obj=student("naman")
print(obj.college)
obj.change_college("IIT kanpur")
print(obj.college)
        
#static method-is used to perform any operation or task without creating any object of that class
class student:
    college="IIT"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_college(cls,new_college):
        cls.college=new_college
    @staticmethod
    def sum(a,b):
        print(a+b)
student.sum(1,2)





    
        

