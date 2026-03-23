# dictnarory is the mutable datatype in python which stores the key and the value pairs.
#keys-are immutable
#values-are mutable
# dictionary syntax
#{"key":"value"}

#initalization
d={}
print(type(d))

d={"key":4}
print(d)

# usecase-dictnarory-use to store details
student_details={
    "name":"jigyasha",
    "location" : "jaipur",
    "mobile" : 23456
}
print(student_details)
# to access any value using key from the dictnonary we use this syntax 
print(student_details["name"])
print(student_details["location"])
print(student_details["mobile"])

# builtin function
student_details.get("name")
#we can access the values from dictnary using .get method
#.get("key")->return value
#dict_name["key"]->return value

#updating a value in dict
#we can update the values
#dict_name["key"]="new_value"
student_details["mobile"]=23489


# to add a new key and value
# we can update a dict and can add key and value
student_details["batch"]="A26"

#.key method is used to check all the keys of the dictionary
student_details.key()
#.value method is used to find all the values which are present into the dictionary
student_details.values()
#.item method is used find the key and the value pairs into the list of tuple
#(key,value)
student_details.item()# it gives list of tuple
#remove any key from dict->pop
# remove any item from a dict->popitem()


# itirating over dict
for value in student_details:
    print(student_details[value])

#using .key
for key in student_details.key():
    print(student_details[key])

#student_details.item()
for item in student_details.item():
    print(item)


for key,value in student_details:
    print(f"{key}->{value}")



employee={
    "name":"rahul",
    "department":"IT",
    "exp":2,
    "location":"jaipur",
    "mobile":34567
}
print(employee)

employee["age"]=34
print(employee)
employee["location"]="udaipur"
print(employee)

all_items = employee.items()
print(all_items)

# wap to count how many element are present in a dictnory
count=0
dict={
    "name":"jigyasha",
    "age":19
}
for value in dict:
    count+=1
print(count)

dict={
    "name":"jigyasha",
    "age":19
}
print(dict.pop("age"))
print(dict.popitem())

# swap keys and values pair in a dict
dict={
    "a":1,
    "b":2,
    "c":3
}
new={}
for key,value in dict.items():
    new[value]=key
print(new)
# using membership operator
for key in dict:
    new[value]=key
print(new)

# find the largest value from the dictnary
dict={
    "a":20,
    "b":30,
    "c":19,
    "d":12
}
lar=0
for value in dict.values():
    if value>lar:
        lar=value
print(lar)

for key in dict:
    if lar<dict[key]:
        lar=dict[key]
print(lar)

# for negative numbers
dict={"a":-1,"b":-2,"c":-9}
lar=float("-inf")
for key in dict:
    if lar<dict[key]:
        lar=dict[key]
print(lar)

#for the smallest number
dict={"a":-1,"b":-2,"c":-9}
lar=float("-inf")
for value in dict:
    if lar<dict[value]:
        lar=dict[value]
print(lar)

dict={"a":-1,"b":-2,"c":-9}
lar=float("-inf")
for key in dict.keys():
    if lar<key:
        lar=key
print(key)

dict={"a":1,"b":5,"c":4}
lar=0
lar_key=""
for key in dict:
    if lar <dict[key]:
        lar=dict[key]
        lar_key=key
print(lar_key)


# count all the occurances of the element of the list
li=[1,1,2,3,3,3,4,4,5,5]
dict={}
for ele in li:
    if ele not in dict:
        dict[ele]=1
    else:
        dict[ele]+=1
print(dict)

# print the duplicates in the list
li=[1,1,2,3,3,3,4,4,5,5]
dict={}
for ele in li:
    if ele not in dict:
        dict[ele]=1
    else:
        dict[ele]+=1
for key,value in dict.items():
    if value>1:
        print(key)

str="this is the place where i born and this is famous for dal baat"
s=str.split()
d={}
for word in s:
    if word not in d:
        d[word]=1
    else:
        d[word]+=1
print(d)

# create a dictnarory from two list
k=[1,2,3,4,5]
v=[20,30,40,50,60]
d={}
for i in range(len(k)):
    d[k[i]]=v[i]
print(d)

print(v[0])
#merge two dict
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d = {}

for key in d1:
    d[key] = d1[key]

for key in d2:
    d[key] = d2[key]

print(d)

# find the commom key between two dict 
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 4, 'c': 5, 'd': 6}
for key in d1:
    if key in d2:
        print(key)




