#encapsulation in python is a core object oriented programming concept that ivolves bundling data(attributes) am=nsd method that operate on that data into a single unit.

# encapsulation is the way to wrap the data and variable and method into the single unit(class) so that it access could be restricted.

#arreibutes in encapsulation
#1.private attribute-are the attributes which is not accessible outside of the class
#it is inatialized with doulbe underscore followed by the arrtibute name
#ex-Bank balance,password etc..

#name mangling-way to access private and protected attribute 
#syntax-private attribute-obj._class.__attribute_name
#syntax-protetedd

# marks management system
class student:
    def __init__(self,name,marks,id):
        self.__marks=20 #private attribute
        self._mobile=234567 #
obj=student("vishal","aosdin")


class ATM:
    def __init__(self,pin,name,balance):
        self.__pin=pin
        self.name=name
        self._balance=balance
    # getter method is used to get the values of the private and protected attribute of the class.
    def dispaly_blance(self):# this display method is accessing the proatected attribute
        balance=self._balance
        print(f"the blance is :{balance}")
    # to change the pin of the atm card
    #this change pin is setter method which is used to set or change or update the value of the private attribute.
    def change_pin(self,new_pin):
        self.__pin=new_pin
        print("pin changed successfully!")
# creating the pin of the card
obj=ATM(1234,"Vivek",5000)
print(obj._ATM__pin) # name mangling

#account management system
#name,balance->private
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def display_balance(self):
        balance=self.__balance
        print(balance)
    def deposite(self,amount):
        self.__balance+=amount
        print("money deposited successfully")

    



#opening account
acc1=BankAccount("rahul",500)
acc1.display_balance()
acc1.deposite(5000)
acc1.display_balance()

#create a class libraryBook that demostrate the encapsulation 
#create a private variable.no_avl_books
#make a method to issue a book(decrease the number of book if books are available otherwise print the " not available book")
#make a method to check how many booka are available.

class LibraryBook:
    def __init__(self, total_books):
        # private variable
        self.__no_avl_books = total_books

    # method to issue a book
    def issue_book(self):
        if self.__no_avl_books > 0:
            self.__no_avl_books -= 1
            print("Book issued successfully.")
        else:
            print("Not available book")

    # method to check available books
    def check_available_books(self):
        print(f"Available books: {self.__no_avl_books}")


# Example usage
library = LibraryBook(3)

library.check_available_books()  # 3
library.issue_book()             # issue 1
library.issue_book()             # issue 2
library.issue_book()             # issue 3
library.issue_book()             # no books left

library.check_available_books()  # 0




# employee salary
class Employee:
    def __init__(self,name,designation,salary,location):
        self.emp_name=name
        self.post=designation
        self.__salary=salary
        self.location=location
    def check_salary(self):
        salary=self.__salary
        print(f"the current salary is :{salary}")
    def change_salary(self):
        self.__salary=new_salary
        print("new salary updated!")
        
emp1=Employee("ajay","ml engineer",25,"jaipur")
emp1.check_salary()
emp1.change_salary(30)
emp1.check_salary()


