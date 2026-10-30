def sort_(arr):
    length=len(arr)
    for i in range(length-1):
        min_index=i
        for j in range(i+1,length):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
print(sort_([5, 2, 9, 11, 10, 8, 7]))