#38. Print numbers from 1 to 50 but skip multiples of 4 using a while loop.
i=1
while(i<=50):
    if i%4==0:
        i+=1
        continue
    print(i)
    i+=1