#Write a program that takes a list of integers and uses map to return a new list containing the square of each number.\
li=[1,2,3,4,5]
def square(n):
    return n**2
print(list(map(square,li)))

#Given a list of temperatures in Celsius, use map to convert them into Fahrenheit. (Formula: F =(C × 9/5) + 32)
def fahre(c):
    return ((c*9/5)+32)
li=[10,20,30]
print(list(map(fahre,li)))

#Take a list of strings and use map to convert each string into its uppercase form.
def upper(s):
    return s.upper()
li=["apple","mango","bananna"]
print(list(map(upper,li)))

#Given a list of numbers, use map with a lambda function to add 10 to each element and print the updated list.
li=[1,2,3,4]
print(list(map(lambda x:x+10,li)))

#Write a program that takes two lists of equal length and uses map to return a list containing the sum of corresponding elements.
li1 = [1, 2, 3, 4]
li2 = [5, 6, 7, 8]
result = list(map(lambda x, y: x + y, li1, li2))
print(result)
