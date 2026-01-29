#21. Print numbers from 1 to 30 but skip numbers between 10 and 20.
for i in range(1,31):
    if(i>=10 and i<=20):
        continue
    print(i)