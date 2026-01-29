#Print numbers from 1 to 100 and stop when you encounter the first number divisible by 7.
for i in range(1,100):
    if i%7==0:
        break
    print(i)