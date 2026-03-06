#1 Create a tuple containing five different numbers and display it.
t=(1,2,4,6,5)
for i in range(len(t)):
    print(t[i])

#2 Access the first and last element of a tuple.
t=(1,2,3,4,5)
print(t[0],t[-1])

#3 Find the total number of elements present in a tuple.
t=(1,2,3,4,5)
count=0
for i in range(len(t)):
    count+=1
print(count)

#4 Check whether a given value exists inside a tuple.
t=(1,2,3,4,5)
ele=8
found=False
for i in range(len(t)):
    if t[i]==ele:
        found=True
        break
    
if found==True:
    print("exists")
else:
    print("not exists")

#5 Concatenate two tuples and print the new tuple.
t1=(1,2,3,4)
t2=(5,6,7,8)
t3=()
for i in t1:
    t3+=(i,)
for j in t2:
    t3+=(j,)
print(t3)

#6 Repeat a tuple two times using an operator.
t=(1,2,3,4,5)
new=t*2
print(new)

#7 Find the index of a specific element in a tuple.
t=(1,2,3,4,5)
ele=5
for i in range(len(t)):
    if t[i]==ele:
        print(i)

#8 Count how many times a particular value appears in a tuple.
t=(1,2,2,2,3,4)
ele=2
count=0
for i in range(len(t)):
    if t[i]==ele:
        count+=1
print(count)

#Slice a tuple to display elements from index 1 to 4.
t=(1,2,3,4,5)
print(t[1:5])

#10 Iterate through all elements of a tuple using a loop.
t=(1,2,3,4,5)
for  i in range(len(t)):
    print(t[i])