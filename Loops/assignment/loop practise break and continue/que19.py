#Print numbers from 1 to 60 but skip multiples of 6.
for i in range(1,61):
    if i%6==0:
        continue
    print(i)