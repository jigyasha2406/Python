#25. Print numbers from 1 to 40 and skip numbers divisible by both 2 and 3.
for i in range(1,41):
    if i%2==0 and i%3==0:
        continue
    print(i)