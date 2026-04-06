#abstraction-abstraction in python is a core oops principle used to manage complexity by hiding internal implementation details and exposing only the essential features of an object.

#abstract class-an abstract class is a blueprint for other classes that cannot be instantiated on its own.
#it is used to define tho common interface for a set of subclasses,ensuring they all implement specific methods.
#enforced interface-an abc define set of method that any subclass must implement.if a subclass fails to implement these method python will raise an error
#blueprint for consistency-it ensures that the different classes follow the some contract

#cor component of the abc method
#1.abc class
#2.@abstractmethod

#implementation of abstraction
# in python abs stands for abstraction base class.it is a module in the python standard library used to define blueprint for other classes.
 
#here we have imported the ABC(helper class) and the abstract method from the module abc
from abc import ABC,abstractmethod
#here we have created a vehicle class(interface or abstract base class)
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class car(vehicle):
    def start(self):
        print("The car start!")
    def stop(self):
        print("The car stops")
class petrolCar(vehicle):
    def start(self):
        print("the petrol class is starting")
    def stop(self):
        print("the petrol car stops")

car=car()
petrolCar=petrolCar()
car.stop()
car.start()
petrolCar.stop()
petrolCar.start()


from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposite(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass

class CurrentAccount(BankAccount):
    def deposite(self):
        print("The money has been deposited inthe account")
    def withdraw(self):
        print("The money has been withdrawal")

class SavingAccount(BankAccount):
    def deposite(self):
        print("The money has been deposited inthe account")
    def withdraw(self):
        print("The money has been withdrawal")
        

current=CurrentAccount()
saving=SavingAccount()
saving.withdraw()

    









