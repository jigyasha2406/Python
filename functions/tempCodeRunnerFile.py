def is_prime(num):
    fact=0
    for i in range(1,num+1):
        if num%i==0:
            fact+=1
    if fact==2:
        return True
    else:
        return False
for i in range(2,101):
    if is_prime:
        print(i,end=" ")