# prime means no devided by any one

num=int(input("Enter Number= "))
status=True

for i in range(2,num):
    if num%i==0:
        status=False

if status:
    print(num,"is prime number")