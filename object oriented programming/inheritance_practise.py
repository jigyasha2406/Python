

#1. Vehicle → Car
class vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class car(vehicle):
    def __init__(self,brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type=fuel_type
obj=car("suzuki",20,"petrol")
print(obj.brand)

#2. Person → Teacher
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
obj=teacher("pooja",32,"english")

#3. Employee → Manager
class employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
class manager:
    def __init__(self,emp_id,salary,department):
        super().__init__(emp_id,salary)
        self.department=department
obj=manager(123,25000,"software engineer")

#4. Product → Electronics
class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class electronics(product):
    def __init__(self,name,price,warrenty_year):
        super().__init__(name,price)
        self.warrenty_year=warrenty_year
obj=electronics("fridge",35000,2)

#5. Animal → Dog
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
class dog:
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed
obj=dog("kittu","animal","pomerian")

#6. Account → SavingsAccount
class account:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
class savingAccount(account):
    def __init__(self,acc_no,balance,interest_rate):
        super().__init__(acc_no,balance)
        self.interest_rate=interest_rate
    def display(self):
        print("Account Number",self.acc_no)
        print("Balance:",self.balance)
        print("Interest Rate",self.interest_rate)
obj=savingAccount(12345,25000,"2%")
obj.display()

#7. User → Admin
class user:
    def __init__(self,username,email):
        self.username=username
        self.email=email
class admin(user):
    def __init__(self,username,email,permissions):
        super().__init__(username,email)
        self.permissions=permissions
    def display(self):
        print("username:",self.username)
        print("email:",self.email)
        print("permissions:",self.permissions)
obj=admin("admin123","admin@gmail.com","allowed")
obj.display()

#8. Book → Ebook
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
class ebook(book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size=file_size
    def display(self):
        print("title:",self.title)
        print("author:",self.author)
        print("file_size:",self.file_size)
obj=ebook("alchemist","parlo","10Mb")
obj.display()


#9. Appliance → WashingMachine
class appliance:
    def __init__(self,brand,power):
        self.brand=brand
        self.power=power
class WashingMachine(appliance):
    def __init__(self,brand,power,capacity):
        super().__init__(brand,power)
        self.capacity=capacity
    def display(self):
        print("brand:",self.brand)
        print("power:",self.power)
        print("capacity:",self.capacity)
obj=WashingMachine("LG","2000h","2l")
obj.display()

#10. Shape → Circle
class shape:
    def __init__(self,color):
        self.color=color
       
class circle(shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius=radius
    def display(self):
        print("color:",self.color)
        print("radius:",self.radius)
obj=circle("red",2)
obj.display()

#11. Device → Laptop
class device:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class laptop(device):
    def __init__(self,name, price,ram):
        super().__init__(name,price)
        self.ram=ram
    def display(self):
        print("Name:",self.name)
        print("Price:",self.price)
        print("RAM:",self.ram)
obj=laptop("Lenova",25000,"2GB")
obj.display()
    
#12. Food → Fruit
class Food:
    def __init__(self,name,calories):
        self.name=name
        self.calories=calories
class fruit(Food):
    def __init__(self,name ,calories,vitamin_content):
        super().__init__(name,calories)
        self.vitamin_content=vitamin_content
    def display(self):
        print("name:",self.name)
        print("calories:",self.calories)
        print("vitamin_content:",self.vitamin_content)
obj=fruit("apple", 104,"C")
obj.display()

#13. Company → Startup
class company:
    def __init__(self,name,location):
        self.name=name
        self.location=location
class startup(company):
    def __init__(self,name,location,funding_amount):
        super().__init__(name,location)
        self.funding_amount=funding_amount
    def display(self):
        print("name:",self.name)
        print("location:",self.location)
        print("funding_amount:",self.funding_amount)
obj=startup("care","jaipur",25000)
obj.display()

#14. Movie → WebSeries
class movie:
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
class webseries(movie):
    def __init__(self,title,duration,no_of_season):
        super().__init__(title,duration)
        self.no_of_season=no_of_season
    def display(self):
        print("title:",self.title)
        print("duration:",self.duration)
        print("no_of_season:",self.no_of_season)
obj=webseries("action","2hr",2)
obj.display()
    
#15. Bank → Loan
class Bank:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
class loan(Bank):
    def __init__(self,name,branch,loan_amount):
        super().__init__(name,branch)
        self.loan_amount=loan_amount
    def display(self):
        print("name:",self.name)
        print("branch:",self.branch)
        print("loan_amount:",self.loan_amount)
obj=loan("HDFC","kukas","2lakh")
obj.display()

#16. Course → OnlineCourse
class course:
    def __init__(self,course_name,duration):
        self.course_name=course_name
        self.duration=duration
class onlineCourse(course):
    def __init__(self,course_name,duration,platform):
        super().__init__(course_name,duration)
        self.platform=platform
    def display(self):
        print("course_name:",self.course_name)
        print("duration:",self.duration)
        print("platform:",self.platform)
obj=onlineCourse("data science","2hr","googleMeet")
obj.display()

#17. Game → MobileGame
class game:
    def __init__(self,title,genre):
        self.title=title
        self.genre=genre
class MobileGame(game):
    def __init__(self,title,genre,size):
        super().__init__(title,genre)
        self.size=size
    def display(self):
        print("title:",self.title)
        print("genre:",self.genre)
        print("size:",self.size)
obj=MobileGame("Free Fire","fighting","2kb")
obj.display()

#18. Hospital → Doctor
class Hospital:
    def __init__(self,name,location):
        self.name=name
        self.location=location
class Doctor(Hospital):
    def __init__(self,name,location,specialization):
        super().__init__(name,location)
        self.specialization=specialization
    def display(self):
        print("name:",self.name)
        print("location:",self.location)
        print("specialization:",self.specialization)
obj=Doctor("SDMH","Jaipur","dermat")
obj.display()
        
#19. Transport → Bus
class Transport:
    def __init__(self,mode,fare):
        self.fare=fare
        self.mode=mode
class Bus(Transport):
    def __init__(self,mode,fare,route_number):
        super().__init__(mode,fare)
        self.route_number=route_number
    def display(self):
        print("mode:",self.mode)
        print("fare:",self.fare)
        print("route_number:",self.route_number)
obj=Bus("road",200,"2A")
obj.display()

#20. Clothing → Shirt
class Clothing:
    def __init__(self,brand,size):
        self.brand=brand
        self.size=size
class Shirt(Clothing):
    def __init__(self,brand,size,color):
        super().__init__(brand,size)
        self.color=color
    def display(self):
        print("brand:",self.brand)
        print("size:",self.size)
        print("color:",self.color)
brand=input("Enter brand:")
while True:
    size=input("Enter size(S/M/L/XL):")
    if size in ["S","M","L","XL"]:
        break
    else:
        print("Invalid size!")
color=input("Enter color:")
obj=Shirt(brand,size,color)
obj.display()
    
        
    


    
    




















