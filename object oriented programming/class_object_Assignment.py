#1. Create a class called Student that has a class attribute school_name andinstance attributes name and age which are initialized using a constructor. Createthree objects and print both the class attribute and instance attributes for each object.
class Student:
    school_name="ABC"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"school_name:{self.school_name}")
        print(f"name:{self.name}")
        print(f"age:{self.age}")
student1=Student("rahul",19)
student1.display()

#2. Create a class called Car that has a class attribute wheels set to 4. Use aconstructor to initialize instance attributes brand and price. Create two objects andshow how both objects share the same class attribute but have different instance attributes.
class Car:
    wheels=4
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"Brand:{self.brand}")
        print(f"Price:{self.price}")
        print(f"Wheels:{self.wheels}")
car1=Car("suzuki",25000)
car2=Car("Nexon",45000)
car1.display()
print()
car2.display()

#3. Create a class called Employee that has a class attribute company_name.Initialize instance attributes emp_name and salary using a constructor. Createmultiple employee objects and print their details along with the common company name.

class Employee:
    company_name="TCS"
    def __init__(self,emp_name,salary):
        self.emp_name=emp_name
        self.salary=salary
    def display(self):
        print(f"Company_name:{self.company_name}")
        print(f"Employee name:{self.emp_name}")
        print(f"Salary:{self.salary}")
emp1=Employee("Rahul",25000)
emp1.display()
print()
emp2=Employee("Anjali",34000)
emp2.display()

#4. Create a class called Mobile that has a class attribute category set toElectronics. Use a constructor to initialize mobile_name and RAM. Create three objects and print all values to clearly understand class vs instance attributes.
class Mobile:
    category="Electronics"
    def __init__(self,mobile_name,RAM):
        self.mobile_name=mobile_name
        self.RAM=RAM
    def display(self):
        print(f"Category:{self.category}")
        print(f"Mobile_name:{self.mobile_name}")
        print(f"RAM:{self.RAM}")
mobile1=Mobile("samsung a26","20gb")
mobile2=Mobile("Xiomi","18gb")
mobile3=Mobile("redmi","30gb")
mobile1.display()
print()
mobile2.display()
print()
mobile3.display()
print()

#5. Create a class called Book that has a class attribute library_name. Initializeinstance attributes title and author using a constructor. Create at least two objects and print their complete information.

class Book:
    library_name="abc"
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f"Library name:{self.library_name}")
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
book1=Book("Alchemist","paol")
book2=Book("Atomic Habits","parl")
book1.display()
print()
book2.display()

#6. Create a class called Laptop that has a class attribute warranty_years. Use aconstructor to initialize brand and price. Create multiple laptop objects and displayhow the class attribute remains same for all objects.
class Laptop:
    warranty_years=4
    def __init__(Self,brand,price):
        Self.brand=brand
        Self.price=price
    def display(self):
        print(f"Brand:{self.brand}")
        print(f"Price:{self.price}")
        print(f"warrenty year:{self.warranty_years}")
laptop1=Laptop("Lenovo",25000)
laptop2=Laptop("ASUS",25000)
laptop1.display()
print()
laptop2.display()        

#7. Create a class called Person that has a class attribute country. Initialize instanceattributes name and age using a constructor. Create three person objects and print their data.
class Person:
    country="India"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Country:{self.country}")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
person1=Person("Anjali",23)
person2=Person("Namrata",22)
person3=Person("Jigyasha",20)
person1.display()
print()
person2.display()
print()
person3.display()

#8. Create a class called Bike that has a class attribute type set to Two Wheeler.Use a constructor to initialize bike_name and mileage. Create objects and print all details.
class Bike:
    Type="Two-wheeler"
    def __init__(self,bike_name,milege):
        self.bike_name=bike_name
        self.milege=milege
    def display(self):
        print(f"Bike name:{self.bike_name}")
        print(f"Milege:{self.milege}")
        print(f"Type:{self.Type}")
bike1=Bike("TVS",20)
bike2=Bike("Honda",30)
bike1.display()
print()
bike2.display()

#9. Create a class called Movie that has a class attribute industry set to Bollywood.Initialize instance attributes movie_name and rating using a constructor. Create multiple movie objects and print the details.
class Movie:
    industry="Bollywood"
    def __init__(self,movie_name,rating):
        self.movie_name=movie_name
        self.rating=rating
    def display(self):
        print(f"Movie:{self.movie_name}")
        print(f"Rating:{self.rating}")
        print(f"Industry:{self.industry}")
movie1=Movie("3 idiots",5)
movie2=Movie("Dangal",5)
movie1.display()
print()
movie2.display()

#10. Create a class called BankAccount that has a class attribute bank_name. Usea constructor to initialize account_holder and balance. Create two account objects and print their information showing both class and instance attributes.
class BankAccount():
    bank_name="HDFC"
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def display(self):
        print(f"Bank name:{self.bank_name}")
        print(f"Account Holder:{self.account_holder}")
        print(f"Balance:{self.balance}")
person1=BankAccount("Anjali",25)
person2=BankAccount("Namrata",30)
person1.display()
print()
person2.display()
