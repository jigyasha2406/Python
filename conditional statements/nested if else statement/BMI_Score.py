#23.Write a Python program that accepts a BMI value and categorizes it as underweight, normal, overweight, or obese.
score=float(input("Enter your BMI score"))
if(score<18.5):
    print("underweight")
elif(score>=18.5 and score<25):
    print("normal")
elif(score>=25 and score<30):
    print("Overweight")
else:
    print("Obese")