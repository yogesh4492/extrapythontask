""" Patten mask """

row=int(input("Enter Row= "))
spc=row-1
for i in range(1,row+1):
    for j in range(1,i+1):
        if i==1 or i==row or j==1 or j==i:
            print("*",end=" ")
        else:
            print(end="  ")
    for k in range(1,spc*4+1):
        print(end=" ")
    for h in range(1,i+1):
        if i==1 or i==row or h==1 or h==i:
            print("*",end=" ")
        else:
            print(end="  ")
        
    print()
    spc-=1
spc=1
for i in range(row-1,0,-1):
    for j in range(1,i+1):
        if i==1 or i==row or j==i or j==1:
            print("*",end=" ")
        else:
            print(end="  ")
    for k in range(1,spc*4+1):
        print(end=" ")
    for h in range(1,i+1):
        if i==1 or i==row or h==i or h==1:
            print("*",end=" ")
        else:
            print(end="  ")
        
        
    print()
    spc+=1