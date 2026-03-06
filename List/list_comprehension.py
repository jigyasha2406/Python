# list comprehension is a concise way to generate a list by using for loop and some condition
# syntax-[expression for expression in range() some condition]

num=[x for x in range(101,0,-1) if x%2==0]
print(num)

# generate a list of odd number from 1 to 100
num=[x for x in range(1,101) if x%2!=0]
print(num)

# generate the square of all the numbers from 1 to 10
num=[x**2 for x in range(1,11)]
print(num)

# generate a list of words which has length 4
li=["apple","car","elephant","dog","cat"]
ch=[word for word in li if len(word)<4]
print(ch)

#generate a new list which has numbers greater than 10
li=[1,2,3,4,5,6,7,8,9,10,11,12,15,17]
gre=[x for x in li if x>10]
print(gre)

# generte the list of odd numbes from 100 to 1
num=[x for x in range(100,0,-1) if x%2!=0]
print(num)

#deep copy and shallow copy
# in shallow copy the reference of the outer objects are different and inner object refernce are same.Thats why when make changes into the copies list then also the change would be reflected into the original list

# in deep copy the nested object are also copied and it dosent change when we make changes into the copies list.
import copy
li=[[1,2],3,4]
deep=copy.deepcopy(li)
deep[0][0]=100
print(deep)
print(li)

# implement deep copy and shallow copy
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