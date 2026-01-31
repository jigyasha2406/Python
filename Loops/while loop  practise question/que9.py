#Write a program to check whether a number is an Armstrong number using a while loop.
num = 153
temp = num
sum = 0
digits=0
while temp>0:
    digits+=1
    temp//10
temp=num

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
