# Q 8: Write a function that accepts a list of numbers and returns the average of the numbers.
# def list_numbers(number_list):
#     sum=0
#     for i in number_list:
#         sum+=i
#     average=sum/len(number_list)
#     return average


# lst1=[x for x in range(1,6)]
# print(list_numbers(lst1))

def average(list1):
    return sum(list1)/len(list1)


lst1=[x for x in range(1,11)]
print(average(lst1))