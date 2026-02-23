#List Creation & Basics
#1 Create a list of 5 integers and print it.
li=[1,2,3,4,5]
print(li)
#2 Create a list of 3 different data types and print each element.
li=[1,"hello",True]
print(li)
#3 How do you check the length of a list? Write a small example.
li=[1,2,3,4,5,6]
print(len(li))
#4 Create an empty list and add three elements to it.
li=[]
li.extend([2,3,4])
print(li)
#using append
li=[]
li.append(2)
li.append(7)
li.append(8)
print(li)


#List Indexing
#1 Create a list of 6 numbers and print the first element.
li=[4,5,3,6,7,8]
print(li[0])
print(li[-1])
print(li[2])
print(li[0:3])
print(li[::-1])



#List Mutability
#1 Create a list and change the second element to a new value.
li=[2,3,4,5]
li[1]=8
print(li)
#2 Replace the last element of a list with 100.
li[-1]=100
print(li)
#3 Modify multiple elements in a list using slicing.
li[0:2]=[7,8]
print(li)




#List Methods (append, extend, insert)
#1 Create a list and use append() to add one element.
li=[3,4,5,6]
li.append(0)
print(li)
#2 Use extend() to add multiple elements to a list.
li=[3,2,4,5]
li.extend([2,4,8,9])
print(li)
#3 Use insert() to add an element at index position 2.
li=[3,4,5]
li.insert(1,8)
print(li)
#4 What is the difference between append() and extend()?
# The one of the major difference between append and extend is that through append we can add only one  element at a time in a list and through extend function we can add multiple element in a list.






#Loop with List
#1 Print all elements of a list using a for loop.
li=[2,3,4,5,6]
for i in range(len(li)):
    print(li[i],end=" ")
    
#2 Print only even numbers from a list using a loop.
li=[2,3,4,6]
even=[]
for i in range(len(li)):
    if li[i]%2==0:
       even.append(li[i])
print(even)

#3 Count how many numbers are greater than 10 using a loop.
li=[3,4,5,6,7,78,45,34]
count=0
for i in range(len(li)):
    if li[i]>=10:
        count+=1
print(count)

#4 Find the sum of all elements in a list using a loop.
li=[2,3,4,5,6]
sum=0
for i in range(len(li)):
    sum=sum+li[i]
print(sum)

#5 Find the maximum element in a list without using max().
li=[3,4,5,6,9]
print(max(li))