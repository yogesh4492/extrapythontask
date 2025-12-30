#armstrong means pow of each and every single digit of given number
num=int(input("ENter Number= "))
copy=num
temp=num
digit=0
sum=0
while num!=0:
    num//=10
    digit+=1

# print(digit)

for i in range(1,digit+1):
    rem=copy%10
    power=pow(rem,digit)
    sum+=power
    copy//=10

if sum==temp:
    print("Armstrong")
else:
    print("Not Armstrng")

