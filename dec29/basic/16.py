# Q 16: Write a function that accepts a number and returns the sum of its digits.

def sum_of_digit(num):
    sum=0
    while num!=0:
        rem=num%10
        sum+=rem
        num//=10
    return sum

num=int(input("Enter Number = "))
print(f"sum of {num} all digits is = {sum_of_digit(num)}")