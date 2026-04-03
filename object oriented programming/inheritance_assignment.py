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
    



  
