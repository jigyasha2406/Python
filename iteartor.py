# itearator-in python iterator is a object allow you to travese throgh all the element of a collection (like a tuple and list) one at a time.unlike a container that holds all datat in memory, an iterator represent a stream of data and retrive items only when requested making it highly memory efficient.
li=iter([x for x in range(100)]) #the list in this is the iterable
print(next(li))#this is the iterator
print(next(li))
print(next(li))

#difference between the iterator anf iterables
#an iterable is a container that can be looped over
#an iterator is an object representing a stream of data that actually performs iteration using next() to retive eements one at a time ,keeping track of its state.



#genrator- a generator is a type of function that returns a lazy iterator allowing you to iterate over a sequence of value without storing the entire dataset in memory at once.
# lazy evaluation
#state preservation 
#automatic iterator protocol



def generate_num():
    li=[x for x in range(20000)]
    for x in range(0,200):
        if li[x]%2==0:
            yield li[x]
obj=generate_num()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


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

