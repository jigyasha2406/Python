n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n=1
for i in range(5):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()
    
n=10
for i in range(5):
    for j in range(i):
        print(n,end=" ")
        n-=1
    print()
    
n=1
for i in range(5):
    for j in range(i):
        if n%2!=0:
            print(n,end=" ")
            n+=1
        n+=1
    print()

n=19
for i in range(5):
    for j in range(i):
        if n%2!=0:
            print(n,end=" ")
            n-=1
        n-=1
    print()

n=2
for i in range(5):
    for j in range(i):
        if n%2==0:
            print(n,end=" ")
            n+=1
        n+=1
    print()

n=20
for i in range(5):
    for j in range(i):
        if n%2==0:
            print(n,end=" ")
            n-=1
        n-=1
    print()

n=4
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


               
num = 1
for i in range(4, 0, -1):
    for j in range(1, i+1):
        print(num, end=" ")
    print()
    num += 1

n=4
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(n,end=" ")
    print()
    n-=1

n=1
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(n,end="")
        n+=1
    print()

n=10
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(n,end=" ")
        n-=1
    print()


n=1
for i in range(4,0,-1):
    for j in range(1,i+1):
        if n%2!=0:
            print(n,end=" ")
            n+=1
        n+=1
    print()

n=19
for i in range(4,0,-1):
    for j in range(1,i+1):
        if n%2!=0:
            print(n,end=" ")
            n-=1
        n-=1
    print()
                  
n=2
for i in range(4,0,-1):
    for j in range(1,i+1):
        if n%2==0:
            print(n,end=" ")
            n+=1
        n+=1
    print()

n=20
for i in range(4,0,-1):
    for j in range(1,i+1):
        if n%2==0:
            print(n,end=" ")
            n-=1
        n-=1
    print()
n = 4

for i in range(1, n+1):
    # Print spaces
    for s in range(n - i):
        print(" ", end="")
    
    # Print numbers in reverse
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()

n=4
for i in range(1, n+1):
    # Print spaces
    for s in range(n - i):
        print(" ", end="")
    
    # Print numbers in reverse
    for j in range(i):
        print(i, end="")
    
    print()


num=4
for i in range(1,5):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(num,end=" ")
    print()
    num-=1

num=1
for i in range(1,5):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
    #num+=1

num=10
for i in range(5):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()



num=19
for i in range(5):
    for s in range(4-i):
        print(" ",end=" ")
    for j in range(i):
            print(num,end=" ")
            num-=2
    print()



num=1
for i in range(5):
    for s in range(4-i):
        print(" ",end=" ")
    for j in range(i):
            print(num,end=" ")
            num+=2
    print()


num=19
for i in range(5):
    for s in range(4-i):
        print(" ",end=" ")
    for j in range(i):
            print(num,end=" ")
            num-=2
    print()


num=2
for i in range(5):
    for s in range(4-i): 
        print(" ",end=" ")
    for j in range(i):
            print(num,end=" ")
            num+=2
    print()


num=20
for i in range(5):
    for s in range(4-i):
        print(" ",end=" ")
    for j in range(i):
            print(num,end=" ")
            num-=2
    print()


n = 5
for i in range(1,n+1):
    for j in range(i):
        print(" ", end="")
    
    for k in range(n - i, 0, -1):
        print(k, end="")
    print()

n = 4
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    
    for k in range(i):
        print(i, end="")
    print()

n = 1
for i in range(4, 0, -1):
    for j in range(4-i):
        print(" ", end="")
    
    for k in range(i):
        print(n, end="")
        n+=1
    print()



n = 10
for i in range(4, 0, -1):
    for j in range(4-i):
        print(" ", end=" ")
    
    for k in range(i):
        print(n, end=" ")
        n-=1
    print()

n = 1
for i in range(4, 0, -1):
    for j in range(4-i):
        print(" ", end=" ")
    
    for k in range(i):
        print(f"{n:2}", end=" ")
        #print("{:>2}".format(n), end=" ")
        # 
        n+=2
    print()

n = 2
for i in range(4, 0, -1):
    for j in range(4-i):
        print(" ", end=" ")
    
    for k in range(i):
        print(f"{n:2}", end=" ")
        n+=2
    print()



n = 20
for i in range(4, 0, -1):
    for j in range(4-i):
        print(" ", end=" ")
    
    for k in range(i):
        print(f"{n:2}", end=" ")
        n-=2
    print()


