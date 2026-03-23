#1. Count Character Frequency: Write a function that takes a string and returns a dictionary
#where the key is the character and the value is the number of times that character appears.
#Example: Input 'banana' → Output {'b':1, 'a':3, 'n':2}.
str="banana"
dict={}
for ele in str:
    if ele not in dict:
        dict[ele]=1
    else:
        dict[ele]+=1
print(dict)



#2. Merge Two Dictionaries with Sum: 
d1={"a":10,"b":20}
d2={"b":5,"c":15}
dict={}
for ele in d1:
    if ele not in dict:
        dict[ele]=d1[ele]
    else:
        dict[ele]+=d1[ele]
for ele in d2:
    if ele not in dict:
        dict[ele]=d2[ele]
    else:
        dict[ele]+=d2[ele]
print(dict)

#3 3. Group Words by First Letter

li=["apple","ant","banana","ball"]
dict={}
for ele in li:
    first=ele[0]
    if first in dict:
        dict[first].append(ele)
    else:
        dict[first]=[ele]
print(dict)

#4. Group Numbers by Even and Odd:
li=[1,2,3,4,5]
dict={"even":[],"odd":[]}

for ele in li:
    if ele%2==0:
        dict["even"].append(ele)
    else:
        dict["odd"].append(ele)
print(dict)

#Check if All Values are Unique:
d1={"a":10,"b":34,"c":23}
if len(set(d1.values()))==len(list(d1.values())):
    print("unique")
else:
    print("not unique")