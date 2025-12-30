# Q 6: Write a function that accepts a string and a character, and returns the number of times the character appears in the string.

#using text.count() for single character

# Sample_string=input("Enter Any String == ")
# char=input("Enter Any Character You Want to check==  ")
# num=Sample_string.count(char)
# # print(name)
#using of collection module of python

# from collections import Counter
# sample=input("Enter Any String = ")
# print(Counter(sample))


# # using of dictionaries of python 
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.errors import HttpError
# from googleapiclient.http import MediaUpload
# import typer
# import json
# import csv
# from openpyxl import 
# sample=input("Enter Your String = ")

# Q 6: Write a function that accepts a string and a character, and returns the number of times the character appears in the string.

from collections import Counter

string1=input("Enter String 1 = ")

list=[x for x in string1]
print(list)
freq={}

for i in list:
    freq[i]=freq.get(i,0)+1

print(freq)


print(Counter(list))
