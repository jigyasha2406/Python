#Print numbers from 1 to 30 but skip multiples of 4.
for i in range(1,31):
    if i % 4==0:
        continue
    print(i)