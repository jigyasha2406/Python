#15. Write a program to check whether a number is a perfect number using a while loop.
n=6
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("Perfect Number")
else:
    print("Not perfect")




for i in range(3):
   for j in range(2):
         print(i + j, end=" ")



i = 10
while i > 1:
  i //= 2
print(i, end=" ")

total = 1
for i in range(1, 4):
   total *= i
print(total)


i = 1
while i <= 4:
  print(i*i, end=" ")
i += 1



