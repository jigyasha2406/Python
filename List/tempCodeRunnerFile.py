li=[1,2,1,2,3,4]
new=[]
for el in li:
    if el not in new:
        new.append(el)
print(new)