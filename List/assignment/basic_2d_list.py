#1 Print all elements of a 2D list row-wise.
li=[[1,2,3],[3,4,5]]
for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j],end=" ")
    print()
#2 Print all elements column-wise.
li=[[1,2,3],[3,4,5]]
for j in range(len(li[0])):
    for i in range(len(li)):
        print(li[i][j],end=" ")
    #print()
#3 Find the sum of all elements in a 2D list.
li=[[1,2,3],[3,4,5]]
sum=0
for i in range(len(li)):
    for j in range(len(li[i])):
        sum=sum+li[i][j]
print(sum)

#4 Find the maximum element in a 2D list.
li=[[1,2,3],[2,3,4]]
lar=li[0][0]
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]>lar:
            lar=li[i][j]
print(lar)
#5 5 Find the minimum element in a 2D list.
li=[[1,2,3],[2,3,4]]
min=li[0][0]
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]<min:
            min=li[i][j]
print(min)

#6 Count total number of elements in a 2D list.
li=[[1,2,3],[3,4,5]]
count=0
for i in range(len(li)):
    for j in range(len(li[0])):
        count+=1
print(count)
#7 Print each row of a 2D list separately.
li=[[1,2,3],[3,8,5]]
for row in li:
    print(row)
# or
li=[[1,2,3],[3,4,5]]
for i in range(len(li)):
    print(li[i])

#8 Print each column of a 2D list separately.
li=[[1,2,3],[4,5,6]]

for j in range(len(li[0])):
    col=[]
    for i in range(len(li)):
        col.append(li[i][j])
    print(col)

 #9 Find the sum of each row.
li=[[1,2,3],[3,4,5]]
sum=0
for i in range(len(li)):
    #sum=0
    for j in range(len(li[i])):
        sum+=li[i][j]
    print(i,sum)
#10 Find the sum of each column.
li=[[1,2,3],[3,4,5]]

for j in range(len(li[0])):
    sum=0
    for i in range(len(li)):
        sum+=li[i][j]
    print(j,sum)

#11 Print the main diagonal elements.
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li)):
    for j in range(len(li[i])):
        if i==j:
            print(li[i][j])


#12 Print the secondary diagonal elements.
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li)):
    for j in range(len(li[i])):
        if i+j==2:
            print(li[i][j])

#13 Find the sum of diagonal elements.
li=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in range(len(li)):
    for j in range(len(li[i])):
        if i==j:
            sum+=li[i][j]
        
print(sum)

#14 Count even numbers in a 2D list.
li=[[1,2,3],[4,5,6],[7,8,9]]
count=0
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]%2==0:
            count+=1
print(count)

#15 Count odd numbers in a 2D list.
li=[[1,2,3],[4,5,6],[7,8,9]]
count=0
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]%2!=0:
            count+=1
print(count)

#16 Replace all negative numbers with 0.
li=[[1,2,-4],[2,-4,-6]]
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]<0:
            li[i][j]=0
print(li)

#17 Find the position (row, column) of a given element.
li=[[1,2,3],[3,4,5]]
tar=1
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]==tar:
            print("row:",i,"column:",j)


#18 Check whether a number exists in the 2D list.
li=[[1,2,3],[4,5,6]]
ele=9
found=False
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]==ele:
            found=True
            break
if found==True:
    print("number exists")
else:
    print("not exist")
    
#19 Flatten a 2D list into a single list.
li=[[1,2,3],[3,4,5]]
flat=[]
for i in range(len(li)):
    for j in range(len(li[i])):
        flat.append(li[i][j])
print(flat)