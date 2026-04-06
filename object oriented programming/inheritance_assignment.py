#1. Create two classes Father and Mother with methods skills_father() and skills_mother(). Create a child class Child that inherits from both and prints both skills.

class Father:
    #def __init__(self):
        #pass
    def skill_father(self):
        print("fathers diriving skills")
class mother:
    #def __init__(self):
       # pass
    def skill_mother(self):
        print("mother driving skills")
class child(Father,mother):
    #def __init__(Self):
       # pass
    def display(self):
        self.skill_father()
        self.skill_mother()
obj=child()
obj.display()

#2. Write a program where class Teacher has a method teach() and class Researcher has a method research(). Create a class Professor that inherits from both and uses both methods.

class teacher:
    def teach(self):
        print("the teacher is teaching english")
class Researcher():
    def reasearch(self):
        print("the research is still going on")
class professor(teacher,Researcher):
    def display(self):
        self.teach()
        self.reasearch()
obj=professor()
obj.display()


#3. Create two classes Engine and ElectricSystem with respective methods. Create a class HybridCar that inherits from both and demonstrates both functionalities.
class engine:
    def engine_prop(self):
        print("This vehicle engine")
class Electric:
    def ElectricSystem(self):
        print("this is electric system class")
class Hybrid(engine,Electric):
    def display(self):
            self.engine_prop()
            self.ElectricSystem()
obj=Hybrid()
obj.display()

#4. Implement two classes Writer and Speaker with methods write() and speak(). Create a class Author that inherits from both and calls both methods.

class Writer():
    def writer_cls(self):
        print("this is the writer class")
class Speaker():
    def speaker_cls(self):
        print("This is a speaker class")
class Author(Writer,Speaker):
    def display(self):
        print("inherited both class properties")
        self.writer_cls()
        self.speaker_cls()
obj=Author()
obj.display()
    
#5. Create two parent classes Calculator1 (addition) and Calculator2 (multiplication). Create a child class that uses both operations.
class calculator1:
    def addition(self,a,b):
        self.a=a
        self.b=b
        print(f"Adittion:{a+b}")
class calculator2:
    def multiplication(self,a,b):
        self.a=a
        self.b=b
        print(f"Multiplication:{a*b}")
class both(calculator1,calculator2):
    def display(self):
        self.addition(10,20)
        self.multiplication(10,20)
obj=both()
obj.display()

#6. Demonstrate method overriding in multiple inheritance where both parent classes have a method with the same name.
class a:
    def show(self):
        print("show method form class a")
class b:
    def show(self):
        print("show method for class b")
class c(a,b):
    def show(self):
        print("show method for class c")
obj=c()
obj.show()
  
#7. Create a class A and B with constructors. Create class C inheriting from both and show how constructors are called.
class a:
    def __init__(self):
        print("This is a class a constructor")
class b:
    def __init__(self):
        print("This is a class b constructor")
class c(a,b):
    def __init__(self):
        #super().__init__() calls constructor based on mro

        a.__init__(self)
        b.__init__(self)
        print("class c constrctor")
obj=c()
        
#8. Write a program to demonstrate the Method Resolution Order (MRO) in multiple inheritance.
class a:
    def show(self):
        print("A class method")
class b:
    def show(self):
        print("B class method")
class c(a,b):
    pass
obj=c()
obj.show()
print("MRO:",c.mro())

#9. Create two classes Person and Employee with attributes. Inherit both into Manager and display combined details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
m = Manager("Rahul", 30, 101, 50000)
m.display()

#10. Implement a class SmartDevice that inherits from both Phone and Camera and performs both calling and clicking photos.
class phone:
    def calling(self):
        print("calling")
class camera:
    def camera(self):
        print("clicking photo")
class SmartDevice(phone,camera):
    def display(self):
        self.calling()
        self.camera()
obj=SmartDevice()
obj.display()
    
#      MULTILEVEL INHERITANCE QUESTIONS

#1. Create class Grandparent, Parent, and Child. Add methods in each and show how child accesses all.
class Grandparent:
    def show_gd(self):
        print("I am grandparent")
class parent(Grandparent):
    def show_pa(self):
        print("I am parent")
class child(parent):
    def show_ch(self):
        print("i am a child")
obj=child()
obj.show_gd()
obj.show_pa()
obj.show_ch()

#2. Write a program where Animal → Mammal → Dog and each class has its own method. Call all methods using the Dog class.
class animal:
    def animal(self):
        print("this is the animal class")
class mammal(animal):
    def mammal(self):
        print("this is the mammal class")
class dog(mammal):
    def dog(self):
        print("this is a dog class")
obj=dog()
obj.animal()
obj.mammal()
obj.dog()

#3. Create a class Vehicle, then Car inherits from it, and SportsCar inherits from Car. Add methods at each level.
class vehicle:
    def show_ve(self):
        print("this is the vehicle")
class car(vehicle):
    def show_ca(self):
        print("this is car class")
class sportCar(car):
    def show_sp(self):
        print("this is a sport car class")
obj=sportCar()
obj.show_ve()
obj.show_ca()
obj.show_sp()


#4. Demonstrate constructor chaining in multilevel inheritance using super().
class  Grandparent:
    def __init__(self):
        print("Grandparent constructor")
class parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")
obj=child()

#5. Create a class Shape → Rectangle → Square and calculate area at each level.
class shape():
    pass
class rectangle(shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
        print(f"Area of rectange:{length*breath}")
class Square(rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        print(f"Area of square:{side*side}")
obj=Square(5)

    
#Write a program showing method overriding in multilevel inheritance.
class A:
    def show(self):
        print("This is class A")

class B(A):
    def show(self):
        print("This is class B")

class C(B):
    def show(self):
        print("This is class C")

obj = C()
obj.show()

#Create a class Student → GraduateStudent → PhDStudent and add attributes progressively.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class GraduateStudent(Student):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
        self.degree = degree

class PhDStudent(GraduateStudent):
    def __init__(self, name, age, degree, research_topic):
        super().__init__(name, age, degree)
        self.research_topic = research_topic

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Degree:", self.degree)
        print("Research Topic:", self.research_topic)
obj = PhDStudent("Aman", 28, "MSc", "Artificial Intelligence")
obj.display()

#
class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, acc_no, balance, interest_rate):
        super().__init__(acc_no, balance)
        self.interest_rate = interest_rate
class FixedDepositAccount(SavingsAccount):
    def __init__(self, acc_no, balance, interest_rate, time):
        super().__init__(acc_no, balance, interest_rate)
        self.time = time

    def show_fd(self):
        print("Account No:", self.acc_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)
        print("Time (years):", self.time)


#Create a class Device → Computer → Laptop and show functionality extension.
class Device:
    def power_on(self):
        print("Device is powered ON")

class Computer(Device):
    def compute(self):
        print("Computer is performing computations")

class Laptop(Computer):
    def portable(self):
        print("Laptop is portable and can run on battery")
obj = Laptop()


#Write a program where each class in multilevel inheritance modifies a variable and shows how values change.
class A:
    def __init__(self):
        self.value = 10

    def show(self):
        print("Class A value:", self.value)


class B(A):
    def __init__(self):
        super().__init__()
        self.value += 5 

    def show(self):
        print("Class B value:", self.value)


class C(B):
    def __init__(self):
        super().__init__()
        self.value *= 2 
    def show(self):
        print("Class C value:", self.value)
obj = C()
