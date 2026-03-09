li=[1,2,3,4,5]
dict={"even":[],"odd":[]}

for ele in li:
    if ele%2==0:
        dict["even"].append(ele)
    else:
        dict["odd"].append(ele)
print(dict)