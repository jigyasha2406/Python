#29.Write a Python program that first checks whether three given sides form a valid triangle, and if valid, determines the type of triangle.
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Valid triangle: Equilateral")
    else:
        if a == b or b == c or a == c:
            print("Valid triangle: Isosceles")
        else:
            print("Valid triangle: Scalene")
else:
    print("Not a valid triangle")
