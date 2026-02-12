n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

n=4
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()


n=4
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(1,8):
        if j%2!=0:
            print(j,end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(8,0,-1):
        if j%2!=0:
            print(j,end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(1,9):
        if j%2==0:
            print(j,end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(8,1,-1):
        if j%2==0:
            print(j,end=" ")
    print()

n=1
for i in range(4):
    for j in range(4):
        print(n,end=" ")
        n+=1
    print()

n=16
for i in range(4):
    for j in range(4):
        print(n,end=" ")
        n-=1
    print()

n=1
for i in range(4):
    for j in range(4):
        if n%2!=0:
            print(n,end=" ")
            n+=1
        n+=1
    print()

n=31
for i in range(4):
    for j in range(4):
        if n%2!=0:
            print(n,end=" ")
            n-=1
        n-=1
    print()

n=2
for i in range(4):
    for j in range(4):
        if n%2==0:
            print(n,end=" ")
            n+=1
        n+=1
    print()

n=32
for i in range(4):
    for j in range(4):
        if n%2==0:
            print(n,end=" ")
            n-=1
        n-=1
    print()

