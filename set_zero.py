a=[[7,0,9,11],
   [5,6,7,0],
   [7,8,1,2]]

r=[0]*len(a)
c=[0]*len(a[0])
for i in range(len(r)):
    for j in range(len(c)):
        if a[i][j]==0:
            r[i]=-1
            c[j]=-1

for i in range(len(r)):
    for j in range(len(c)):
        if r[i]==-1 or c[j]==-1:
            a[i][j]=0

print(a)