def partition(num,low,high):

    pivot=num[low]

    i,j=low,high

    while i<j:
        if num[i]<=pivot and i<=high:
            i+=1
        elif num[j]>=pivot and j>=low+1:
            i+=1
        else:
            num[j],num[i]=num[i],num[j]
    num[j],num[low]=num[low],num[j]

    return num

nums = [4, 6, 2, 5, 7, 9, 1, 3]
print(partition(nums,0,7))