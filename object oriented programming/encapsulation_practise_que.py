#1. Create a class Person with a private variable __name. Create methods to set and get the name.
class person:
    def __init__(self,name):
        self.__name=name
    def display_name(self):
        name=self.__name
        print(f"name of the oerson is:{name}")
obj=person("rahul")
obj.display_name()

#2. Create a class BankAccount with private variable __balance. Add methods deposit(amount), withdraw(amount), and get_balance().
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def add_balance(self,amount):
        self.__balance+=amount
        print("Amount successfully added!")
    def withdraw_amount(self,amount):
        self.__balance-=amount
        print("Amount withdrawl")
    def get_balance(self):
        balance=self.__balance
        print(f"Total balance:{balance}")
obj=BankAccount("anjali",25000)
obj.add_balance(10000)
obj.withdraw_amount(5000)
obj.get_balance()
    
#3. Create a class Student with private variable __marks. Add methods to assign and display marks only if marks are greater than 0.
class Student():
    def __init__(self,marks):
        self.__marks=marks
    def assign(self,marks):
        if marks>0:
            self.__marks=marks
        else:
            print("Marks should be greater than 0")
    def get_marks(self):
        if self.__marks>0:
            print(f"Marks:",self.__marks)
        else:
            print("no valid marks to display")
s1=Student(78)
s1.assign(-10)
s1.assign(75)
s1.get_marks()


#4. Create a class Employee with private variable __salary. Add methods to set salary, increase salary by percentage, and get salary.
class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def set_salary(self,new):
        self.__salary+=self.__salary*new/100
        print("salary increased")
    def get_salary(self):
        salary=self.__salary
        print(f"New salary:{salary}")
obj=Employee(25000)
obj.set_salary(10)
obj.get_salary()

#5. Create a class Temperature with private variable __celsius. Add methods to set temperature and convert it to Fahrenheit.
class Temprature:
    def __init__(self,celsius):
        self.__celsius=celsius
    def convert(self):
        fahrenheit=(self.__celsius*9/5)+32
        print(fahrenheit)
obj=Temprature(25)
obj.convert()

#6. Create a class Mobile with private variable __price. Add methods to set price (not negative) and get price.
class Mobile:
    def __init__(self,price):
        self.__price=price
    def set_price(self,price):
        if price>=0:
            self.__price=price
        else:
            print("price cannot be negative")
    def get_price(self):
        print(f"price:{self.__price}")
obj=Mobile(2500)
obj.set_price(25000)
obj.get_price()
        
#7. Create a class Car with private variable __speed. Add methods set_speed(speed <= 200) and get_speed().
class Car :
    def __init__(self,speed):
        self.__speed=speed
    def set_speed(self,speed):
        if self.__speed<=200:
            self.__speed=speed
        else:
            print("the speed is greater than 200")
    def get_speed(self):
        speed=self.__speed
        print(f"the spped:{speed}")
obj=Car(500)
obj.set_speed(500)
obj.get_speed()

#8. Create a class LoginSystem with private variable __password. Add methods to set and validate password.
class LoginSystem:
    def __init__(self,password):
        self.password=password
    def set_pass(self,pwd):
        if len(pwd)>=6:
            self.__password=pwd
            print("password set successfully")
        else:
            print("password must be of 6 character long")
    def validate(self,pwd):
        if pwd==self.__password:
            print("login succesful")
        else:
            print("Incorrect password")
user=LoginSystem("123456")
user.set_pass("123456")
user.validate("123456")

#99. Create a class Product with private variable __quantity. Add methods to add stock, reduce stock (not below 0), and check quantity
class Product:
    def __init__(self):
        self.__quantity = 0   
    def add_stock(self, qty):
        if qty > 0:
            self.__quantity += qty
            print("Stock added")
        else:
            print("Invalid quantity")
    def reduce_stock(self, qty):
        if qty > 0:
            if qty <= self.__quantity:
                self.__quantity -= qty
                print("Stock reduced")
            else:
                print("Not enough stock")
    def check_quantity(self):
        print("Available Quantity:", self.__quantity)

#10. Create a class VotingSystem with private variable __age. Add methods to set age and check if user can vote (>=18).



        
    