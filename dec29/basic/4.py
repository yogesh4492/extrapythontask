# Q 4: Write a function that accepts a list of numbers and returns the maximum value in the list.
# with using of python inbuild function
# def max_value(lst):
#     return max(lst)


# lst1=[x for x in range(1,100,5)]
# print(max_value(lst1))
# print(max(lst1))
# print(min(lst1))

# without  using of python inbuild functions


def max_value(lst):
    maximum_num=lst[0]
    for i in lst:
        if i>maximum_num:
            maximum_num=i
    return maximum_num

def minimum_value(lst):
    min_value=lst[0]
    for i in lst:
        if i<min_value:
            min_value=i
    return min_value

number_list=[]

length=int(input("Enter length of list = "))

for i in range(1,length+1):
    num=int(input("Enter Number = "))
    number_list.append(num)

print(max_value(number_list))
print(minimum_value(number_list))
