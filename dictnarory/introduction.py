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