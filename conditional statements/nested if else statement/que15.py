#Write a Python program that accepts three sides of a triangle and checks whether the triangle is a right-angled triangle.
hypo=int(input("Enter the first side of triangle:"))
pen=int(input("Enter the second side:"))
base=int(input("Enter thr third side:"))
if hypo**2==pen**2+base**2:
    print("Its a right angle triangle")
else:
    print("not a right angle triange")