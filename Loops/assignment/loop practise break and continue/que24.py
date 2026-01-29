#Print numbers from 1 to 100 and stop when you encounter the first even number greater than 50.
 
for i in range(1,101):
    if i>50 and i % 2==0:
        break
    print (i) 