t=(2,3,4,5,6)
lar=0
for i in range(len(t)):
    if t[i]%2!=0:
        if t[i]>lar:
            lar=t[i]
print(lar)
