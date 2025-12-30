# Q 9:Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.

def string_manipulation(string):
    if len(string)>5:
        return string.upper()
    else:
        return string.lower()
    
str1=input("Enter String1 = ")

print(string_manipulation(str1))
