# Q 1: Accept a number from the user and find the factorial of the number using a function with a parameter and return type.
# using of math module of python
# from math import *
# num=int(input("Enter A Number = "))
# print(factorial(num))

# without any build in module

num=int(input("Enter Number 1= "))
fact=1
#normal for loop
# for i in range(1,num+1):
#     fact*=i
# print(fact)

# using of while loop

while num>0:
    fact*=num
    num-=1

print(fact)


