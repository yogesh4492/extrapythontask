# Q 3: Write a function that accepts a list of numbers and returns the sum of all even numbers in the list.

def accept_lst_of_no(lst):
    sum=0
    for i in lst:
        if i%2==0:
            sum+=i
    return sum

lst1=[]
length=int(input("Enter How Many Number You Want To Enter :  "))
# print(length)

for i in range(1,length+1):
    num=int(input("Enter Number = "))
    lst1.append(num)

print(accept_lst_of_no(lst1))