n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n=4
for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4 or (n-i+1)==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=4
#col=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,1+n):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    

n=8
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1, 0,-1):
        for j in range(i):
            print("*",end=" ")
        print()


n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()




n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if(i==1 or i==n or j==0 or j==2*i-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


n=4
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if(i==1 or i==n or j==0 or j==2*i-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i-1):
        if(i==1 or i==n or j==0 or j==2*i-2):
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()


n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if(i==1 or i==n or j==0 or j==2*i-2):
            print(chr(64+i),end=" ")
        else:
            print(" ",end=" ")
    print()


n=4
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if(i==1 or i==n or j==0 or j==2*i-2):
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()


n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()






n = 5  
for i in range(2 * n):
    print("*", end=" ")
print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(1, n):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")
    print()
for i in range(2 * n):
    print("*", end=" ")






n = 5

for i in range(n):
    # Print spaces for alignment
    for j in range(n - i - 1):
        print("  ", end="")

    num = 1
    for j in range(i + 1):
        print(num, end="   ")
        num = num * (i - j) // (j + 1)

    print()


n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print(chr(64+2*i),end=" ")
         
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print(chr(64+2*i),end=" ")
        else:
            print(" ",end=" ")
    print()

n = 6

for i in range(1, n + 1):
    # Print leading spaces (to tilt the shape)
    for j in range(n - i):
        print(" ", end=" ")

    # Print stars and hollow spaces
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(n):
        print("*",end=" ")
    print()
    



n=7
a=0
b=1
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c

n=5
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)

n=7
sum=0
i=1
while i<=n:
    if n%i==0:
        sum+=i
    i+=1
    