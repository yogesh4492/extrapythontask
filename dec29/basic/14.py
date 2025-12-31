# Q 14: Write a function that accepts a list of strings and returns the longest string in the list.

def longest_string(str_lst):
    lon=str_lst[0]
    for i in str_lst:
        if len(i)>len(lon):
            lon=i
    return lon

    
    

string_list=['hello',"how","are","you"]
print(f"Longest String in list : {longest_string(string_list)}")


