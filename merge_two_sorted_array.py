

def sort(left,right,num=[],i=0,j=0):
    if j==len(right):
        num.extend(left[i:])
        return 
    
    if i==len(left):
        num.extend(right[j:])

        return 

    if left[i]<=right[j]:
        if left[i] not in num:
            num.append(left[i])
        sort(left,right,num,i=i+1,j=0)
    
    elif right[j]<=left[i]:
        if right[j] not in num:
            num.append(right[j])
        sort(left,right,num,i=i,j=j+1)

    return num
    

print(sort([1,2,3,6,],[0,1,1,2,4,7,9]))
