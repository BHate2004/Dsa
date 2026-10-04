def _remove_duplicates(num,i=0,j=1):
    if j==len(num):
        return
    if num[i]!=num[j]:
        num[i+1],num[j]=num[j],num[i+1]
        _remove_duplicates(num,i+1,j+1)
    else:
        _remove_duplicates(num,i,j+1)
    return num

print(_remove_duplicates([1,1,2,2,3,4]))