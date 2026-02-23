#find the frequency of each number
li=[1,2,1,1,1,3,3,4,5]
checked=[]
for ele in li:
    if ele not in checked:
        print(ele,"->",li.count(ele))
        checked.append(ele)
                       
#rotate a list left by 1 position
li=[10,20,30,40,50]
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
#3. Find Index of All Occurrences of a Given Element
li=[5,2,7,2,9,2]
target=2
ind=[]

for i in range(len(li)):
    if li[i]==target:
        ind.append(i)
print(ind)

#Remove All Negative Numbers from a List
li=[2,3,-1,9,-9]
new=[]
for i in range(len(li)):
    if li[i]>0:
        new.append(li[i])
print(new)
#7. Find Pairs Whose Sum Equals Target Value
# for index
li=[1,2,3,4,5]
tar=7
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==tar:
            print([i,j])
# for values
li=[2,4,3,5,7]
tar=7
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==tar:
            print(li[i],li[j])

#8. Find Missing Number from 1 to n
li=[1,2,4,5,6]
for i in range(1,len(li)+1):
    if i not in li:
        print(i)
        break
#second method
li=[1,2,4,5,6]
n=len(li)+1
expected=n*(n+1)//2
actual=sum(li)
print(expected-actual)

#9. Remove Elements That Appear More Than Once
li=[1,2,2,3,4,4,5]
new=[]
for ele in li:
    if li.count(ele)==1:
        new.append(ele)
print(new)
