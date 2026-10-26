ar = [3, 1, 5, 2, 4,7, 1, 3, 5, 2, 4, 1, 3]
def b_search(ar,target,low=0,high=len(ar)-1,mid=None):
    if low>high:
        return 'not-found'
    mid=(low+high)//2
    if target==ar[mid]:
        return  ar[mid]
    elif ar[mid]<target:
        return b_search(ar,target,low+1,high,mid=mid)
    elif ar[mid]>target:
        return b_search(ar,target,low,high-1,mid=mid)
print(b_search(ar,9))