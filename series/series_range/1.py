#prime in given range


rang_s=int(input("enter the start point: "))
rang_e=int(input("enter teh end point : "))

for i in range(rang_s,rang_e):
    status =1
    for j in range(2,i):
        if i%j==0:
            status=0
    if status:
        print(i)
