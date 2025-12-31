# Q 15: Write a function that accepts a number and checks if it is an Armstrong number.


def armstrong_number(num):
    temp=num
    sum=0
    digit=0
    while temp!=0:
        temp=temp//10
        digit+=1
        
    for i in range(1,digit+1):
        rem=num%10
        power=rem**digit
        sum+=power
        num//=10

    return sum

    


try:
    num=int(input("Enter Number = "))
    result=armstrong_number(num)
    if num==result:
        print("Number is Armstrong...")
    else:
        print("Number Is Not an Armstrong...",result,num)
except Exception as e:
    print(f"Error : {e}")


    
