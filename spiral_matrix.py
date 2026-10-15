a=[[7,3,9,1],
   [5,6,7,3],
   [7,8,1,2]]
max=len(a[0])-1
lst=[]
for i in range(len(a)):
    if i>0:
        lst.append(a[i][max])
    else:
        if i==0:
            for j in range(len(a[0])):
                lst.append(a[i][j])
print(lst)