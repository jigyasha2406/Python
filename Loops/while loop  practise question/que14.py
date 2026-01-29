#14. Write a program to create a new number by squaring each digit of a given number usinga while loop.
n = 234
new = 0
place = 1

while n > 0:
    digit = n % 10
    sq = digit * digit

    new = sq * place + new

    if sq >= 10:
        place *= 100
    else:
        place *= 10

    n //= 10

print(new)
