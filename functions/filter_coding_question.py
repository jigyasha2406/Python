#Given a list of integers, use filter to create a new list containing only even numbers.
li=[1,2,3,4,5,6]
def is_even(n):
    if n%2==0:
        return True
    return False
print(list(filter(is_even,li)))

#Write a program that takes a list of numbers and filters out all numbers greater than 50.
li=[45,60,89,70]
def greater(n):
    if n>50:
        return True
    return False
print(list(filter(greater,li)))

#Given a list of strings, use filter to return only those strings whose length is greater than 5.
li=["apple","bananan"]
def string(n):
    if len(n)>5:
        return True
    return False
print(list(filter(string,li)))

#Write a program to filter out all negative numbers from a given list using filter and lambda.
li=[1,2,-3,-4]
print(list(filter(lambda x:x<0,li)))

#Given a list of integers, use filter to extract only numbers that are divisible by both 2 and 3.
li=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x%2==0 and x%3==0,li)))
