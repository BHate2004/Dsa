a=[[7,3,9,1],
   [5,6,7,3],
   [7,8,1,2],
   [3,5,6,7]]
rows = len(a)
cols = len(a[0])

rotated_matrix = [[0] * rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        rotated_matrix[j][(rows-1)-i]=a[i][j]
print(rotated_matrix)


