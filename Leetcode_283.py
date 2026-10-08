arr=[0,0,1,0,22,0,2,0,4,0,0,1,2,0,4,2,0,0]

def move_zero_last(num,i=0,j=1):
    if j==len(num):
        return
    if num[i]!=0:
        move_zero_last(num,i+1,j+1)
    if num[i]==0 and num[j]!=0:
        num[i],num[j]=num[j],num[i]
        move_zero_last(num,i+1,j+1)
    if num[i]==0 and num[j]==0:
        move_zero_last(num,i,j+1)
    return num
print(move_zero_last(arr))