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