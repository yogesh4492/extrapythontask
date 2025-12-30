#strong numbersum of every digit factorial of number is == original number

num=int(input("Enter Num= "))
temp=num
sum=0
while num!=0:
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
    num//=10

if sum==temp:
    print("Strong Number")
else:
    print("Not a Strong Number")
