def merge_array(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        elif  right[j]<left[i]:
            result.append(right[j])
            j+=1
    
    if i==n:
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    return result

def _merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[0:mid]
    right=arr[mid:]
    left_array=_merge_sort(left)
    right_array=_merge_sort(right)
    return merge_array(left_array,right_array)
print(_merge_sort([3,1,2,4,1,50,2,6,4]))
