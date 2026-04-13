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