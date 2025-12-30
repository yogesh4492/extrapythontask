# 
# Q 7: Write a function that accepts a list of strings and returns a new list with each string reversed.

def acept_list(org_list):
    rev_list=[]
    for i in org_list:
        rev_list.append(i[::-1])
    return rev_list
    

list1=["hello","jay","how","are"]
print(acept_list(list1))
        



