#Print all numbers from 1 to 100, but skip numbers between 30 and 40.
for i in range(1,101):
    if i>=30 and i<=40:
        continue
    print(i)