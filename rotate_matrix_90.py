a=[[7,3,9,1],
   [5,6,7,3],
   [7,8,1,2],
   [3,5,6,7]]
def rotate_matrix_90(a):
   
    rows = len(a)
    cols = len(a[0])
    for i in range(rows):
        for j in range(i+1,cols):
            a[i][j],a[j][i]=a[j][i],a[i][j]

    for i in range(rows):
        a[i].reverse()
    return a
print(rotate_matrix_90(a))