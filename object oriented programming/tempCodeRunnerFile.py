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
