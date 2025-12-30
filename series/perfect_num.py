#perect means sum of divisabel digit is == original number

num=int(input("Enter Number= "))


sum=0

for i in range(1,num):
    if num%i==0:
        sum+=i

if sum==num:
    print("perfect")