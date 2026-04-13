# tuples-are the datatype in python which stores the collection of herogeneous elemnts.it is immutable in nature
#tuple-stores ordered collection of pair
# inialized with {}
# immutable
# tuple packing
#tuple unpacking

# inatialization
t=(1,2)
print(type(t))

t=(1)
print(type(t))

#use case of tuple
#name of the days
#into the database
#colors->(r,g,b)
# faster  accessing the element than the list


# difference between the list and the tuple]
#list is mutable while the tuple is immutable
#accessing the element into the tuple is faster than the list
#list is initialised with the "[]" and the tuple is intialized with the "{}"

#how to  make changes in a tuple
#since the tuple is immutable in nature .although you want to change the tuple then you have to type cast that tuple into the list then after you can change into the tuple
t=(4,5,6)
li

# tuple packing-is the process in python of automatically grouping multiple values into a single tuple,an immutable and orderd pair
a=1,2
print(type(a))
details="rahul","A26",26
print(details)

# tuple unpacking-ia a python feature that allow you to assign elements from a tuple to multiple variable in a single ,readable line of coode.
#here we are unpacking the values of the tuple into multiple variable
#rule- left side var = no. of element in the tuple
details="rahul","A26",26
name,batch,rollno=details
print(details)
print(name)
print(batch)

#method in tuple
#count,sum,index,max,min
t=(1,2,1,2,1,2,3)
# count method is used to find the no. of frequences of the element
#tuple.count(element)
t.count(1)
# sum method is used to return the sum of list of the element which are stored into the list or tuple
sum(t)
#index-index method is used to find the index of the first occurance of the value
t.index(3)

#iterating a tuple
t=(1,2,3,4)
for i in range(len(t)):
    print(t[i])

for el in t:
    print(el)

# wap to print the sum of odd number and even number separetly from the tuple
t=(1,2,3,4,5,6,7,8,9,10,11,12,13)
even_sum=0
odd_sum=0
for i in range(len(t)):
    if t[i]%2==0:
        even_sum+=t[i]
    else:
        odd_sum+=t[i]
print(even_sum)
print(odd_sum)

# wap to find  the largest
t=(2,3,8,4,5)
lar=0
for i in range(len(t)):
    if t[i]>lar:
        lar=t[i]
print(lar)

t=(2,3,4,5,6)
lar=0
for i in range(len(t)):
    if t[i]%2==0:4 
        if t[i]>lar:
            lar=t[i]
print(lar)

t=(2,3,4,5,6)
lar=0
for i in range(len(t)):
    if t[i]%2!=0:
        if t[i]>lar:
            lar=t[i]
print(lar)


#second largest
li=[1,2,3,4,5,6,7]
first=float("-inf")
second=float("-inf")
for ele in li:
    if ele>first:
        second=first
        first=ele
    elif ele>second:
        second=ele
print(second)

#sorting without sort
li=[2,3,1,5,8,3,1,2]
for i in range(len(li)):
    min_index=i
    for j in range(i+1,len(li)):
        if li[j]<li[min_index]:
            min_index=j
    li[i],li[min_index]=li[min_index],li[i]
print(li)


s="abcabcbb"
max_len=0
for i in range(len(s)):
    substring=[]
    current_sum=0
    start,stop,temp_start=0
    for j in range(i,len(s)):
        if s[j] in substring:
            break
        substring.append(s[j])
        current_sum+=1
        
    if current_sum>max_len:
        max_len=current_sum
print(max_len)


               