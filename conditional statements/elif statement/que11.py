#Write a program using elif to check the type of triangle: Equilateral, Isosceles, or Scalene.
a=int(input("Enter the first side"))
b=int(input("Enter the second side"))
c=int(input("Enter the thirs side"))
if a==b==c:
    print("Its is the equilateral triangle")
elif a==b or b==c or c==a:
    print("Its a Isosceles triangle")
else:
    print("Its a scalalr triangle") 