#14. Print numbers from 1 to 30 but skip multiples of 3.
for i in range(1,31):
    if i%3==0:
        continue
    print(i)