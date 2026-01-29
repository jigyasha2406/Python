#Print numbers from 1 to 40 but skip numbers divisible by 5 using continue.
for i in range(1,41):
    if i%5==0:
        continue
    print(i)