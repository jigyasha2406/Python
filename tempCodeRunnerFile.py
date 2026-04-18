
def generate_num():
   # li=[x for x in range(20000)]
    for x in range(0,200):
        if x%2==0:
            yield x
obj=generate_num()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
