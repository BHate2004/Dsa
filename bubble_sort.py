
def bubble_sort(arr):
    length=len(arr)
    for i in range(length-1):
        for j in range (length-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([50, 200, 90, 1, 10, 8, 7]))
