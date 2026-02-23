li=[1,2,2,3,4,4,5]
new=[]
for ele in li:
    if li.count(ele)==1:
        new.append(ele)
print(new)