import copy
li=[[2,3,4],[3,4,5],1,2]
shallow_list=copy.copy(li)
deep_list=copy.deepcopy(li)
print(shallow_list)
print(deep_list)
deep_list[0][0]=100
shallow_list[0][0]=100
print(shallow_list)
print(deep_list)
print(li)