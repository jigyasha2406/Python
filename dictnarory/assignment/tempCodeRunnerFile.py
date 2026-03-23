#Check if All Values are Unique:
d1={"a":10,"b":34,"c":23}
if len(set(d1.values()))==len(list(d1.values())):
    print("unique")
else:
    print("not unique")