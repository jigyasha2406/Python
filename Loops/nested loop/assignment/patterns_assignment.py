n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(n,0,-1):
    for j in range(i):       print("*",end=" ")
    #for j in range(i):
        #print("*",end=" ")
    print()

n=5
for i in range(n,0,-1):
    for j in range(n-i):       print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

n=4
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

n=4

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i,2*i):
        print(j,end=" ")

    print()
   
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i,2*i):
        print(j,end=" ")
    for j in range(2*i-2,i-1,-1):
        print(j,end=" ")
    print()
    
n=4
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()


n=4
ch=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end=" ")
        ch+=1
    print()

n=9
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print(i,end=" ")
    print()

n=9
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=9
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n=9
for i in range(n,0,-1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
    for j in range(n-1,i-1,-1):
        print(j,end=" ")
    print()

n=9
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()

n=9
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print(i,end=" ")
    print()