#Print numbers from 1 to 50 but skip numbers ending with 3.
for i in range(1,51):
    if i%10==3:
        continue
    print(i)