for i in range(100,0,-1):
    if(i%2==0):
        print("even",i)
    else:
        print("odd",i)

i=1
while i<100:
    if i==10:
        i+=1
        continue
    print(i)
    i+=1


a=10
b=23
a=a+b
b=a-b
a=a-b
print(a)
print(b)

a=10
b=56
a=b
b=a

print(a)
print(b)
