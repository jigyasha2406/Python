#Print numbers from 1 to 100 and stop when the sum crosses 200.
sum=0
for i in range(1,101):
    sum+=i
    if sum>=200:
        break
print(sum)