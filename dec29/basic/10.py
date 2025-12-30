# Q 10: Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.

def divisible_by_3(lst):
    blank_list=[]
    for i in lst:
        if i%3==0:
            blank_list.append(i)
    return blank_list

number_list1=[10,16,14,78,69]

print(divisible_by_3(number_list1))
