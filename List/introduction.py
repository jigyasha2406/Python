# list is a collection for orderd elements
#properties-mutable,ordered,allowes duplicates,stors hetrogeneous elements
# denoted by square brackets

#intialization
li=[]
print(type(li))

#hetrogenous element
li=[1,False,2,None,"string"]
print(li)

# ordered pairs
# you can access it through index
li=[2,3,4]
print(li[0])
#the index should be in the range,otherwise it will give an erroe that list in out of range

#accessing elemts through loops
li=[2,3,4,5]
for  i in range(len(li)):
    print(li[i])

#using the membership operator we can accesses all the elemnet of the list,list are iterable
li=[2,3,4,5]
for ele in li:
    print(ele)

# sum of the elements of a list
sum=0
li=[1,2,3,4]
for i in range(len(li)):
    sum=sum+li[i]
print(sum) 
#using membership operator
li=[1,2,3,4]
res=0
for ele in li:
    res=res+ele
print(res)


# some method to add elements into the list
#append
#extend()
#insert()
li=[1,2,3,4]
# append method is used to add the element at th end of the list
li.append(5)
#extend
li1=[5,6,7,8]
# extend method is used to add multiple element at the last of the last
li.extend(li1)
print(li)
li=[2,3,4,0]
li.extend([1,2]) #li.extend(1,2)-will not work
print(li)

#paricular index
# insert method is used to insert the element on a particular element
#list_name.insert(index,value)
li=[1,2,3]
li.insert(0,100)
print(li)

# find the largest element from the list 
li=[2,3,8,4]
lar=0
for i in range(len(li)):
    if li[i]>lar:
        lar=li[i]
print(lar)
#separate out the even and odd element fromn the list
number=[2,1,3,4]
even=[]
odd=[]
for num in number:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)

#product of all the elements 
prod=1
li=[2,3,4,5]
for i in range(len(li)):
    prod=prod*li[i]
print(prod)

#insert ,append,extend
li=[1,2,3,4]
li.append(7)
print(li)
li=[1,2,3,4]
li.extend([2,6,8,9])
print(li)
li=[9,5,6]
li.insert(2,34)
print(li)
#find the particular elemt from the list
li=[2,3,4,5]
ele=78
pre=False
for num in li:
    if num==ele:
        found=True
        break
if pre==True:
    print("element in the list")
else:
    print("element not in the list")


#tuple->list
t=(1,2,3)
li=list(t)
print(li)

# removing element from the list
#pop,remove,clear

#1.pop-pop method removes the particular element index from the list
#by default it return the last element
#syntax-list_name.pop(index)
li=[1,2,3]
li.pop(0)
print(li)

#2.remove-remove element is used to remove the particular element from the list
#syntax-list_name.remove(element)
#remove method does not return anything
li=[2,3,4]
li.remove(2)

#3.clear-clear method is used to remove all the element from the list
li.clear()


#sort,sorted,reverse,max,min,sum,count

#sort()-method is used to sort the original list

#sorted(li)->sorted function is used to sort the values into the new list
#max()-gives the maximum value
#min()-gives the minimum value
#count()-method is used to return the number of occurances of the particular element from the list
li=[1,1,1,1,1,1,2,2,2,3,3,3]
print(li.count(1))
print(li.count(2))
print(li.count(3))

#wap to print the qoccurance of a particular element

li=[1,1,1,1,2,2,2,3,3]
print(li.count(1))

li=[1,1,1,1,2,2,2,3,3]
count=0
for i in range(len(li)):
    if li[i]==1:
        count+=1
print(count)

# reverse the list
li=[1,1,1,2,3,3,4,4,5]
print(li[::-1])
li = [1, 4, 5, 6]
rev = []
for i in range(len(li)):
    rev.append(li.pop())
print(rev)
# second method
li=[4,5,6,8]
rev=[]
for i in range(len(li)-1,-1,-1):
    rev.append(li[i])
print(rev)
#third method-using swaping
li=[2,3,4,5]
left=0
right=len(li)-1
while(left<right):
    li[left],li[right]=li[right],li[left]
    left=left+1
    right=right-1
print(li)

#product except self
li=[2,3,4,5,0]
pro=[]
prod=1
for i in range(len(li)):
    prod=prod*li[i]
for i in range(len(li)):
    #pro_self=prod//li[i]
    pro.append(prod//li[i])
print(pro)

#count even numbers
li=[1,2,3,4]
count=0
for i in range(len(li)):
    if li[i]%2==0:
        count+=1
print(count)

#common element between two list
li=[2,3,4,5]
li2=[1,3,4,5]
common=[]
for el in li:
    if el in li2:
        common.append(el)
print(common)

li=[2,3,4,5]
li2=[1,3,4,5]
common=[]
for el in li:
    if (el in li2) and el not in common:
        common.append(el)
print(common)

#remove duplicates frm the list
li=[1,2,1,2,3,4]
new=[]
for el in li:
    if el not in new:
        new.append(el)
print(new)

# find max and min from the list
li = [1,2,3,4,5]
min = li[0]
max = li[0]
for ele in li:
    if ele <min:
        min= ele
    if ele> max:
        max = ele
print(min)
print(max)

#find the second largest in a list
li=[2,1,3,4,6]
li.sort()
print(li)

li = [1, 2, 2, 3, 4, 6, 5]

first_largest = 0
second_largest = 0

for i in range(len(li)):
    if li[i] > first_largest:
        second_largest = first_largest
        first_largest = li[i]
    elif li[i] > second_largest and li[i] != first_largest:
        second_largest = li[i]

print(second_largest)

#"this is a sentence"-reverse the words of the string
s = "this is a sentence"
words = s.split()
new= []
for word in words:
    new.append(word[::-1])
print(" ".join(new))

#rotate a list left by 1 position
li=[1,2,3,4,5]
k=2
left=0
right=len(li)-1
while(left<right):
    li[left],li[right]=li[right],li[left]
    left=left+1
    right=right-1
left=0
right=k-1
while(left<right):
    li[left],li[right]=li[right],li[left]
    left=left+1
    right=right-1
left=k
right=len(li)-1
while(left<right):
    li[left],li[right]=li[right],li[left]
    left=left+1
    right=right-1
print(li)

#print the index of target sum
li=[1,2,3,4,5]
tar=7
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==tar:
            print([i,j])
    
#print th product of positive numbers
li=[1,2,-3,4,-7]
prod=1
for i in range(len(li)):
    if li[i]>0:
        prod=prod*li[i]
print(prod)

#2-D list
li=[[1,2,3],[8,9,7]]
print(li[0][0])

#accessing all the elements
li=[[1,2,3],[8,9,7]]
for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j],end=" ")

#print the sum of all the elements of the 2d list
li=[[1,2,3],[8,9,7]]
sum=0
for i in range(len(li)):
    for j in range(len(li[i])):
        sum+=li[i][j]
print(sum)
 