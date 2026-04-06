li=[1, 2, 3, 4, 2, 5, 6, 3, 7, 1]
s=set()
dup=set()
for ele in li:
    if ele in s:
        dup.add(ele)
    else:
        s.add(ele)
print(list(dup))