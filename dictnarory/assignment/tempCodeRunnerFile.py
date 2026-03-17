li=["apple","ant","banana","ball"]
dict={}
for ele in li:
    first=ele[0]
    if first in dict:
        dict[first].append(ele)
    else:
        dict[first]=[ele]
print(dict)