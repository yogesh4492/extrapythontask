# Q 2: Write a function that accepts a string and returns True if the string is a palindrome, and False otherwise.


def accept_string(str):
    if str==str[::-1]:
        return True
    else:
        return False
def accept(string1):
    rev=""
    for i in string1:
        rev=i+rev
    if rev==string1:
        return True
    else:
        return False    

str=input("Enter Any String = ")
# str="hello"
# rev=""
# for i in str:
#     rev=i + rev
#     print(rev)
# print(rev)
# print()
print(accept(str))
print(accept_string(str))
# from abc import ABC,abstractmethod

# # @abstractmethod
# class Main(ABC):
#     pass
#     # def __init__(self):
#     #     pass

# class Sub(Main):
#     def __init__(self):
#         print("From abc import Abstarct class")

# if __name__=="__main__":
#     obj=Main()