# Q 11: Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.


list1=[7,5,4,3,6,4,3]
# square_list=[x**2 for x in list1]
# print(square_list)

def squares_list(org_list):
    result_list=[]
    for i in org_list:
        result_list.append(i*i)
    return result_list

print(squares_list(list1))

