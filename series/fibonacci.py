#means sum of two past digit

num=int(input("Enter Number= "))

n1=0
n2=1

print("Fibonaccis eriez is :",n1,n2,end=" ")
for i in range(1,num-1):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
