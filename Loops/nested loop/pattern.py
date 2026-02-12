for i in range(1,5):
    for j in range(4):
        print(i,end=" ")
    print()

for i in range(4):
    for j in range(1, 5):
        print(j, end="")
    print()

for i in range(4):
    for j in range(i,i+1):
        print(j,end=" ")
    print()

num = 1
for i in range(4):      
    for j in range(4): 
        print(num, end=" ")
        num += 1
    print()

for i in range(4, 0, -1):
    for j in range(4):
        print(i, end="")
    print()

for i in range(4):
    for j in range(4, 0, -1):
        print(j, end="")
    print()

for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()

n=1
for i in range(1,5):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()


for i in range(4):
    for j in range(4):
        print(chr(65+j),end=" ")
    print()


for i in range(4):
    for j in range(4):
        print(chr(65+j),end=" ")
    print()


ch = 65
for i in range(4):        
    for j in range(4):   
        print(chr(ch), end=" ")
        ch += 1
    print()


for i in range(4):
    for j in range(4):
        print(chr(65+j),end=" ")
    print()


for i in range(4):
    for j in range(4):
        print(chr(68-j),end=" ")
    print()


for i in range(4):
    for j in range(4):
        print(chr(68-i),end=" ")
    print()
#second method
for i in range(3,-1,-1):
    for j in range(4):
        print(chr(65+i),end=" ")
    print()
    
for i in range(4,0,-1):
    for j in range(4):
        print(chr(68-j),end=" ")
    print()


for i in range(1, 5):
    for j in range(i):
        print(chr(65+j), end="")
    print()

ch=65
for i in range(1,5):
    for j in range(i):
        print(chr(ch),end=" ")
        ch+=1
    print()

for i in range(1, 5):
    for j in range(i):
        print(chr(69-i), end="")
    print()
#or
for i in range(0,i+1):
    for j in range(0,i+1):
        print(chr(65+(n-1)-i),end=" ")
    print()

for i in range(5):
    for j in range(i):
        print(chr(64+i), end="")
    print()


for i in range(4,0,-1):
    for j in range(i):
        print(chr(64+i), end="")
    print()

for i in range(5):
    for j in range(4):
        print(chr(64+i),end=" ")
    print()

for i in range(4,0,-1):
    for j in range(i):
        print(chr(69-i), end="")
    print()

for i in range(4,0,-1):
    for j in range(i):
        print(chr(64+i), end="")
    print()

n=4
for i in range(1,n+1):
    # logic for printing spaces
    for j in range(n-i):
        print(" ",end=" ")
    # logic for printing star
    for j in range(i):
        print("*",end=" ")
    print()


n=4
for row in range(1,n+1):
    for col in range(row):
        print("*",end=" ")
    print()
for row in range(n-1)


n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for st in range(2*i-1):
        print("*",end=" ")
    print()


                 
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for st in range(2*i-1):
        print(i,end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end=" ")
    for st in range(2*i-1):
        print(st+1,end=" ")
   
    print()

n=int(input('enter n= ')) 
for  i in range (1, n+1):
    for sp in range (n-i):
       print(' ',end=' ')
    for num  in range (1,2*i):
        print(n-i+1,end=' ')
    print( )

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    
    for n in range(i-1,0,-1):
        print(n,end=" ")
    print()


n=4
for row in range(1,n+1):
    for sp in range(n-row):
        print(" ",end=" ")
    for num in range(1,row+1):
        print(num,end=" ")
    for num in range(row-1,0,-1):
        print(num,end=" ")
    print()

ch=64
n=4
for row in range(1,n+1):
    for sp in range(n-row):
        print(" ",end=" ")
    for ca in range(1,row+1):
        print(chr(ch+ca),end=" ")
    for ca in range(row-1,0,-1):
        print(chr(65+ca),end=" ")
    print()
              
ch=64
n=4
for row in range(1,n+1):
    for sp in range(n-row):
        print(" ",end=" ")
    for ca in range(1,row+1):
        print(chr(ch+ca),end=" ")
    for ca in range(row-1,0,-1):
        print(chr(ch+ca),end=" ")
    print()
            

n= 4
ch= 65
for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end=' ')
    for j in range(2*i-1):
        print(chr(ch),end=' ')
    ch+=1
    print()

n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
    for j in range(1,n):
        print(" ",end=" ")
    for k in range(2*(n-i)-1):
        print("*",end=" ")
    print()

n = 3
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print(i, end="")
    
    print() 
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print(i, end="")
    
    print() 


n = 3
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print(i, end="")
    
    print() 
for i in range(1,n):
    for j in range(i):
        print(" ", end="")
    for k in range(2*(n-i)-1):
        print(i, end="")
    
    print() 


n=4
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(2*(n-i)-1):
        print("*", end="")
    
    print() 
for i in range(1, n+1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


n = 5
for i in range(1,n+1):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n - i, 0, -1):
        print("*", end=" ")
    print()
for i in range(1,n-1):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
  

n = 4
for i in range(n, 0, -1):
    
    for j in range(n - i):
        print(" ", end=" ") 
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(2, n + 1):
    
    for j in range(n - i):
        print(" ", end=" ")
    
    for k in range(i):
        print("*", end=" ")
    print()


ch=64
n=4
for i in range():
    
    for j in range(n - i):
        print(" ", end=" ") 
    for k in range(i):
        print(chr(64+i), end=" ")
    print()
for i in range(2, n+ 1):
    
    for j in range(n - i):
        print(" ", end=" ")
    
    for k in range(i):
        print(chr(68-j), end=" ")
    print()

n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()