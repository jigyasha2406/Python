#Create a base class Animal with a method sound(). Then create three child classes Dog, Cat, andCow that override the sound() method to print their respective sounds. Write a main program where youcreate objects of each class and call the sound() method using a parent class reference to demonstrate runtime polymorphism.
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

#Create a base class Vehicle with a method start(). Then create child classes Car, Bike, and Truckthat override the start() method with their own implementation. Demonstrate how the correct method is called at runtime when using a common reference.
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

#3. Create a base class Shape with a method area(). Then create child classes Circle and Rectangle.Override the area() method in both classes to calculate their respective areas. Use dynamic methoddispatch to call the correct area() method.

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

#Create a base class Employee with a method salary(). Then create subclasses FullTimeEmployeeand PartTimeEmployee. Override the salary() method in each subclass to calculate salary differently.Demonstrate runtime polymorphism using these classes.

class Employee:
    def salary(self):
        print("Salary is not defined")
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def salary(self):
        print("Full-Time Employee Salary:", self.monthly_salary)
class PartTimeEmployee(Employee):
    def __init__(self, hours, rate_per_hour):
        self.hours = hours
        self.rate_per_hour = rate_per_hour

    def salary(self):
        total_salary = self.hours * self.rate_per_hour
        print("Part-Time Employee Salary:", total_salary)
emp1 = FullTimeEmployee(50000)
emp2 = PartTimeEmployee(20, 500)
emp1.salary()
emp2.salary()

#5. Create a base class Bank with a method interest_rate(). Then create subclasses SBI, HDFC, andICICI. Each subclass should override the interest_rate() method with different values. Write a program to show polymorphic behavior.
class Bank:
    def interest_rate(self):
        print("Interest rate not defined")
class SBI(Bank):
    def interest_rate(self):
        print("SBI Interest Rate: 6%")
class HDFC(Bank):
    def interest_rate(self):
        print("HDFC Interest Rate: 7%")
class ICICI(Bank):
    def interest_rate(self):
        print("ICICI Interest Rate: 6.5%")
b1 = SBI()
b2 = HDFC()
b3 = ICICI()
b1.interest_rate()
#6. Create a base class Payment with a method pay(amount). Then create subclassesCreditCardPayment, UPIPayment, and CashPayment that override the pay() method with differentlogic. Show how runtime polymorphism works when calling the method.
class Payment:
    def pay(self, amount):
        print("Payment method not defined")
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} in Cash")
p1 = CreditCardPayment()
p2 = UPIPayment()
p3 = CashPayment()
p1.pay(20)

#Create a base class Notification with a method send(message). Then create subclassesEmailNotification, SMSNotification, and PushNotification. Each subclass should override the send()method. Demonstrate polymorphism using a loop.

class Notification:
    def send(self, message):
        print("Notification not defined")
class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent with message: {message}")
class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent with message: {message}")
class PushNotification(Notification):
    def send(self, message):
        print(f"Push Notification sent with message: {message}")
n1 = EmailNotification()
n2 = SMSNotification()
n3 = PushNotification()
n1.send("hello")


#Create a base class Media with a method play(). Then create subclasses Audio, Video, and Podcast.Override the play() method in each subclass. Show how different play() methods are called dynamically.
class Media:
    def play(self):
        print("Playing media")
class Audio(Media):
    def play(self):
        print("Playing audio file")
class Video(Media):
    def play(self):
        print("Playing video file")
class Podcast(Media):
    def play(self):
        print("Playing podcast episode")
m1 = Audio()
m2 = Video()
m3 = Podcast()
m1.play()

#Create a base class User with a method access_level(). Then create subclasses Admin, Editor, andViewer. Override the access_level() method to return different permissions. Demonstrate runtime polymorphism.
class User:
    def access_level(self):
        return "No access defined"
class Admin(User):
    def access_level(self):
        return "Full access (read, write, delete)"
class Editor(User):
    def access_level(self):
        return "Edit access (read, write)"
class Viewer(User):
    def access_level(self):
        return "Read-only access"
u1 = Admin()
u2 = Editor()
u3 = Viewer()
print(u1.access_level())

#Create a base class Appliance with a method turn_on(). Then create subclasses Fan, AC, andWashingMachine. Override the turn_on() method with specific behavior. Show polymorphism using acollection of objects.
class Appliance:
    def turn_on(self):
        print("Appliance is turned on")
class Fan(Appliance):
    def turn_on(self):
        print("Fan is spinning")
class AC(Appliance):
    def turn_on(self):
        print("AC is cooling")
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is washing clothes")
a1 = Fan()
a2 = AC()
a3 = WashingMachine()
a1.turn_on()










    
        

        

