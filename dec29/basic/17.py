# Q 17: Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.

print("hello".swapcase())# using of inbuild function

def swapcase_string(string):
    swap_string=""
    for i in string:
        if i.isupper():
            swap_string+=i.lower()
        else:
            swap_string+=i.upper()
    return swap_string

str1=input("Enter String = ")
print(f"Swap String = {swapcase_string(str1)}")
