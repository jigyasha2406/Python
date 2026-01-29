

#sum of the numbers
#sum=1
#for i in range(1,6):
    #sum *= i 
#print(sum)

#print the numbers from 43 to 100 using step 3
#for i in range(43,101,3):
    #print(i)
#print all the even numbers from 100 to 1
#for i in range(100,0,-2):
    #print(i)
#
#for i in range(100,0,-1):
    #if(i%2==0):
        #print("even",i)
    #else:
        #print("odd",i)

#for i in range(1,100)
    #if i%2==0:
        #print("even",i)

#pro=1
#for i in range(1,6):
   # pro *= i
#print(i)


n = 8
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)


sum=0
for i in range(2,100):
    if i%2==0:
        sum+=i
print(sum)

sum=0
for i in range(2,100):
    if i%2!=0: 
        sum+=i
print(sum)

prod=1
for i in range(40,36,-1):
    if i%2==0:
        prod*=i
print(prod)


n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)



st="Rahul"
for i in range(4,-1,-1):

    print(st[i])


sto="python"
for i in range(0,len(st)):
    if i%2!=0:
        print(sto[i])


name="python"
for i in range(0,len(name),3):
    print(name[i])

#factorial
for i in range(1,11):
    if i%3!=0:
        print(i)

#using continue statement 
#continue ststement is used to skip the current iteartion for some condition

for i in range(1,11):
    if i%3==0:
        continue
    print(i)

for i in range(2,200):
    if i%2==0:
        continue
    print(i)


for i in range(1,41):
    if i>10 and i<15:
        continue
    print(i)

for i in range(1,21):
    if i%2==0 and i%3==0:
        continue
    print(i)

# break statement is used to break the loop (Stop iteration)
for i in range(5,51):
    if i==25:
        break
    print(i)

for i in range(5,50):
    if i%10==7:
        break
    print(i)

sum=0
for i in range(1,11):
    sum+=i
    if sum==15:
        break
    print(sum)
 
count=0
for i in range(1,16):
    if(i%3==0 and i%5==0):
        count+=1
    print(count)

for i in range(1,101):
    if i%10==6:
        continue
    print(i)

    
i=0
# here we gave the ondition to run the loop
#this loop will run until the condition become false
while(i<5):
    print(i)
    i=i+1         
i=5
while(i>1):
    print(i)
    i=i-1

i=1
while i<100:
    if i==75:
        break
    print(i)
    i=i+1

i=1
while i<100:
    if i==10:
        i+=1
        continue
    print(i)
    i+=1
