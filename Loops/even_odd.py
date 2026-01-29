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
