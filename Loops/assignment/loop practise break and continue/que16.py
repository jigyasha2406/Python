#Print numbers from 1 to 100 and stop when a number ends with 7.
for i in range(1,101):
    if i%10==7:
        break
    print(i)