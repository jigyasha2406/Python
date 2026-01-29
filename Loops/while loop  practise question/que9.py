#Write a program to check whether a number is an Armstrong number using a while loop.
num = 153
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
