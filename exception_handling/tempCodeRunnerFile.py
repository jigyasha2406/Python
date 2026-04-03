try:
    a="10"
    b=20
    c=a+b
     
except TypeError as e:
    print("something is hapend",e)
else:
    print(c)
finally:
    print("this block will always run ")