matrix = [
    [13, 12, 11, 10, 9,15]
]
def spiral_matrix(matrix):
    left=0
    top=0
    right=len(matrix[0])-1
    bottom=len(matrix)-1
    while top<=bottom and  left<=right:
        # right to left
        for i in range(left,right+1):
            print(matrix[top][i])
        top+=1
        print()
        # top to bottom
        for i in range(top,bottom+1):
            print(matrix[i][right])
        right-=1
        print()
        # bottom right to left
        if  top<=bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i])
            bottom-=1
        print()
        # bottom to top
        for i in range(bottom,top-1,-1):
            print(matrix[i][left])
        left+=1

spiral_matrix(matrix)