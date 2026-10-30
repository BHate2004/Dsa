nums=[-2,5,6,4,0,9,10,7,]
def _insertion_sort(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            for j in range(i+1,0,-1):
                if arr[j]<arr[j-1]:
                    arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr

            

print(_insertion_sort(nums))