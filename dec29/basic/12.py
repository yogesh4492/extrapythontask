# Q 12: Write a function that accepts a string and counts how many vowels are in the string.


def vowel_list(strin1):
    count=0
    for i in strin1:
        if i in "aeiou":
            count+=1

    return count

string=input("Enter String = ")

print(f" no of vowel in string is {vowel_list(string)}")

