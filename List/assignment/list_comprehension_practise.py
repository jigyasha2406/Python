#Create a list of numbers from 1 to 10 using list comprehension.
nums=[x for x in range(1,11)]
print(nums)

#Create a list containing squares of numbers from 1 to 10.
nums=[x**2 for x in range(1,11)]
print(nums)

#• Create a list containing cubes of numbers from 1 to 10.
nums=[x**3 for x in range(1,11)]
print(nums)

#• Generate a list of even numbers from 1 to 20.
nums=[x for x in range(1,21) if x%2==0]
print(nums)

#• Generate a list of odd numbers from 1 to 20.
nums=[x for x in range(1,21) if x%2!=0]
print(nums)

#Create a list of numbers divisible by 3 from 1 to 30.
nums=[x for x in range(1,31) if x%3==0]
print(nums)

#Create a list of numbers greater than 10 from a given list.
nums=[x for x in range(1,21) if x>10]
print(nums)

#From a list of numbers, create a new list containing only positive numbers.
li=[1,2,3,-3,-4,-7,8,9]
nums=[x for x in li if x>0]
print(nums)

#From a list, create a list containing only negative numbers.
li=[1,2,3,-3,-4,-7,8,9]
nums=[x for x in li if x<0]
print(nums)

#• Create a list of numbers whose square is greater than 50.
nums=[x for x in range(1,21) if x**2>50]
print(nums)

#Convert all words of a list into uppercase using list comprehension.
words=["apple","banana","grapes"]
upper=[word.upper() for word in words]
print(upper)

#Convert all words of a list into uppercase using list comprehension.
words=["apple","banana","grapes"]
lower=[word.lower() for word in words]
print(lower)

#Create a list containing length of each word from a list of strings.
words=["apple","banana","grapes"]
length=[len(word) for word in words]
print(length)

#Extract only words having more than 4 characters.
words=["apple","banana","grapes"]
length=[word for word in words if len(word)>5]
print(length)
