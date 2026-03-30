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
    def add_balance(self):
        balance=
    