""" Map Function that map the result based on function 
its contain two parameter:

map(function,iterable)
their is function based map the data 
by default its return map object convert it into list also for working

"""

def double(w):
    return w*2
lis=[1,2,3,4,5]
res=map(double,lis)
print(list(res))
