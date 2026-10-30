arr=[3,9,5,6,7,2]
def rotate_k(arr,k,count=0):
    if k>len(arr) and count==0:
        k=k%len(arr)
    if k==len(arr):
        return arr
    if k==count:
        return arr
    return rotate_k([arr[-1]]+arr[:-1],k,count+1)

print(rotate_k(arr,7))