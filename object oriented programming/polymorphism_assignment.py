class sound():
    def make_sound(self):
        print("diffrent animal make different sound")
class dog(sound):
    def make_sound(self):
        print("Barks")
class cat(sound):
    def make_sound(self):
        print("meow")
class cow(sound):
    def make_sound(self):
        print("woo")
dog=dog()
cat=cat()
cow=cow()
cow.make_sound()
cat.make_sound()
dog.make_sound()


class vehicle():
    def start(self):
        print("the vehiche is starting")
class car(vehicle):
    def start(self):
        print("the car is starting")
class bike(vehicle):
    def start(self):
        print("The bike is starting")
class truck(vehicle):
    def start(self):
        print("The truck is starting")
car=car()
bike=bike()
truck=truck()
car.start()
bike.start()
truck.start()


class shape():
    def area(self):
        print("calcutating the area")
class circle(shape):
    def __init__(self,r):
        
        self.r=r
    def area(self):
        pi=3.14
        print("area:",pi*self.r,self.r)
class rectangle(shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        print("area",self.length*self.breath)
circle=circle(20)
circle.area()






 init




    
        

        

