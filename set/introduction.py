# set -> set ia a collection of unique elements which stores the element into the unorded manner
#sets is mutable
# # it stores the hetrogneous elements
# we cant index over the sets.
#inatized using curly braces
s={1,2,"aman",1,2,"anam"}
type(s)
#emplty set-we cannot inatilized empty set with the curly braces
# we can inatized empty set with a set constructor
s=set()
print(type(s))

#creating set from the list
li=[1,2,3,1,3,4]
print(set(li))

#in set we store immutable datatype
s={1,4}
s={[2,3],1,1}# it will give error

#accessing set elemnts-we can not use range function in it.
s={1,2,3,4}
for ele in s:
    print(ele,end=" ")

#123456
s={1,2,3,4,5,6,7,8,9,10}
even=0
odd=0
for ele in s:
    if ele%2==0:
        even+=ele
    else:
        odd+=ele
print(even)
print(odd)

#remove the duplicates from the list
li=[1,2,3,2,3,1]
s=set(li)
print(s)

#remove the duplicates from the tuple
t=(1,2,3,3,2,4)
s=set(t)
print(s)

#remove the duplicate character from the string
str="this is a programming class"
str.split()
s=set(str)
print("".join(str))
  
#find the common element from a two set
s={1,2,3,4}
s1={3,4,5,6}
for ele in s:
    if ele in s1:
        print(ele)

#operations on sets
#intersection-it is used to find commom element between two or more  sets
s1={1,2,3,4,5}
s2={3,4,5,6}
s3={3,4,5,0}
print(s1.intersection(s2))
print(s1 & s2 & s3)

#union
s1={1,2,3,4,5}
s2={3,4,5,6}
s3={3,4,5,0}
print(s1 | s2 | s3)
print(s1.union(s2).union(s3))

#difference
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1-s2)

#symmetric difference-it removes the common elements between two sets
s1={1,2,3,4,5}
s2={1,2,3,7,8}
print(s1.symmetric_difference(s2))
print

# .add()-add one element into the set
s={1,2,3,4}
s.add(9)
print(s)

#.update()-add multiple elemment into the set
s={1,2,3,4,5}
s.update([8,9])
print(s)



# remove a element from the set ->pop(),remove(),discard()
# pop method is used to remove any elemnt or to remove random element
# remove method is used to remove a specific element ,if that element is not present in the set it will give a error ,which error is known as key error
#discard -this method is used to remove a element from the set,and if the number we have to remove is not present in the set it wil not threw a error
s={1,2,3,4,5}
print(s.pop())

s={1,2,3,4,5}
s.remove(4)
print(s)

s={1,2,3,4}
s.discard(5)
print(s)

s="pythonprogramming"
unique_ele=set()
unique_word=""
for c in s:
    if c not in unique_ele:
        unique_ele.add(c)
        unique_word+=c
print(unique_word)
print(unique_ele)

