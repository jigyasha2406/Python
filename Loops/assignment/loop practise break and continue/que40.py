#40. Print numbers from 1 to 40 but stop when a number ends with 9 using a while loop.
i=1
while(i<=40):
    if i%10==9:
        break
    print(i)
    i+=1


