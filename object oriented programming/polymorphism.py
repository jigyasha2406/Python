#polymorphism-it is the one of the most important pillar of oops in which a function or method have many forms 
#poly means many,morphism means form 
#two types-compile time polymorphism(method overloading)
#         - run time polymorphism(method overriding)

#compiletime polymorphism-method overloading is a compiletime polymorphism feature where class has multiple method with the same name but different parameter. 
#

#why python does not support compile time overloading-
#python does not support traditional method overloading due to its dynamic nature and the way it mange name(name overwriting)
#we can achive overloding in python by - using variable length argument
#                                      - default parameters


#method overriding(runtime polymorphism)- method overidding in python is oops concept where a subclass provide its own specific implementation of a method that is already defined in its parent class.python support method overriding.
class animal:
    def make_sound(self):
        print("animal makes sound")
class dog (animal):
    def make_sound(self):
        print("Barks")
obj=dog()
obj.make_sound()


class PaymentSyatem:
    def pay_amount(self):
        print("the payment has been done")
    def summary(self):
        print("the summary of the order")

class CreditCard(PaymentSyatem):
    def pay_amount(self):
        print("Payment has been don ethrougn credit card")

class UpiPayment(PaymentSyatem):
    def pay_amount(self):
        print("Payment has been done through upi")
card=CreditCard()
upi=UpiPayment()
card.pay_amount()
upi.pay_amount()
upi.summary()
card.summary()





 



