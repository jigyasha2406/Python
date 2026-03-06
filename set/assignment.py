#1. Create a set of numbers from 1 to 5 and print it.
s={1,2,3,4,5}
for ele in s:
    print(ele)

#2. Add an element to an existing set.
s={1,2,3,4,5}
s.add(7)
print(s)

#3. Remove an element using remove() and observe what happens if the element does not exist.
s={1,2,3,4,5}
s.remove(6)
print(s)
# it will give an error

#4. Remove an element using discard() and compare the behavior with remove().
s={1,2,3,4,5}
s.remove(6)
print(s) # remove will give an error if the number not exists in the set
s={1,2,3,4,5}
s.discard(7)
print(s) # discard will not throw an error if the element is not present in the list

#5. Find the length of a set.
s={1,2,3,4,5}
print(len(s))


#6. Check if a specific element exists in a set.
s={1,2,3,4,5}
spe=6
pre=False
for ele in s:
    if ele==spe:
        pre=True
        break
if pre==True:
    print("present")
else:
    print("not present")

        
#7. Clear all elements from a set.
s={1,2,3,4,5}
s.clear()
print(s)

#8. Convert a list with duplicate values into a set to remove duplicates.
li=[1,1,2,3,3,4,5,5,6]
s=set(li)
print(s)


#9. Create an empty set correctly (without using {}).
s=set()
print(type(s))

#10. Iterate through a set and print each element.
s={1,2,3,4,5,6}
for ele in s:
    print(ele)

#11 11. Given two sets, find their union.
s1={1,2,3,4}
s2={2,3,4,5,6}
print(s1.union(s2))
print(s1|s2)

#12 12. Given two sets, find their intersection.
s1={1,2,3,4}
s2={2,3,4,5,6}
print(s1.intersection(s2))
print(s1&s2)

#13 13. Find the difference between two sets.
s1={1,2,3,4}
s2={2,3,4,5,6}
print(s1-s2)

#14. Find the symmetric difference between two sets.
s1={1,2,3,4,5}
s2={3,4,5,6}
print(s1.symmetric_difference(s2))

#15 15. Check whether one set is a subset of another.
s={1,2,3}
s2={1,2,3,4}
print(s<=s2)
print(s.issubset(s2))

#16 16. Check whether one set is a superset of another.
s={1,2,3}
s2={1,2,3,4}
print(s>=s2)
print(s.issuperset(s2))

#17 17. Check whether two sets are disjoint.
s={1,2,3}
s1={3,4,5}
print(s.isdisjoint(s1))

#18 18. Update one set with another set.
s1={1,2,3,4,5}
s2=(6,7,8,9)
s1.update(s2)
print(s1)

#19. Remove a random element from a set.
s1={1,2,3,4,5}
s1.pop()
print(s1)

#20. Find common elements between three sets.
s1={1,2,3}
s2={3,4,5}
s3={3,8,9}
print(s1.intersection(s2).intersection(s3))

#21 Given a sentence, find all unique characters using a set.
sent=" this is a sentence"
s=set(sent)
print(s)

#22 Count the number of unique words in a paragraph using a set.
sent="this is a programming class"
s=set(sent)
print(len(s))

#23. Given two lists, return a list of common unique elements using sets.

li=[1,2,3,4,5]
li1=[3,4,6,7,8]
common=list(set(li) & set(li1))
print(common)
# without operator
common = []
for i in li:
    if i in li1 and i not in common:
        common.append(i)
print(common)

#Find elements that appear in either of the two sets but not in both.
s1={1,2,3,4}
s2={3,4,5,6}
print(s1^s2)

#Given a list of numbers, find all duplicate elements using sets.
li=[1, 2, 3, 4, 2, 5, 6, 3, 7, 1]
s=set()
dup=set()
for ele in li:
    if ele in s:
        dup.add(ele)
    else:
        s.add(ele)
print(list(dup))

#26. Write a program to check if two strings are anagrams using sets.





#27. Given a set of numbers, remove all even numbers.
s={2,3,4,5,6,7}
for ele in s.copy():
    if ele%2==0:
        s.remove(ele)
print(s)
#or
se={ele for ele in s if ele%2!=0}
print(s)

#28. Create a set comprehension to generate squares of numbers from 1 to 10.
se={ele for ele in range(1,11)}
print(se)

#29 From a given set, create a new set containing only numbers greater than 10.
s={14,35,67,3,4,5,6,67}
sc={ele for ele in s if ele>10}
print(sc)

#30. Given multiple sets in a list, find the intersection of all sets.
s1={1,2,3,4}
s2={3,4,5,6}
s3={3,4,7,8,9}
print(s1 & s2 & s3)
