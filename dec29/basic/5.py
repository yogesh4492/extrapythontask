# Q 5: Accept a number from the user and check if it is a prime number using a function with a parameter and return type.

def check_prime(num):
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
    return flag

num=int(input("Enter A Number = "))

result=check_prime(num)
if result:
    print(f"{num} is Palindrome Number")
else:
    print(f"{num} is not a Palindrome Number")
