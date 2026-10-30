nums=[1,2,3,4,6,6,7,8,9,9,9]

def lower_no(nums,target,low=0,high=len(nums)-1,mid=None,lower=-1):
    if low>high:
        return lower
    mid=(low+high)//2
    if nums[mid]>=target:
        return lower_no(nums,target,low=low,high=mid-1,mid=mid,lower=mid)
    elif nums[mid]<target:
        return lower_no(nums,target,low=mid+1,high=high,mid=mid,lower=lower)
    



def upper_no(nums,target,low=0,high=len(nums)-1,mid=None,upper=-1):
    if low>high:
        return upper
    mid=(low+high)//2
    if nums[mid]<=target:
        return upper_no(nums,target,low=mid+1,high=high,upper=mid)
    elif nums[mid]>target:
        return upper_no(nums,target,low=low,high=mid-1,upper=upper)

def find_occur(nums,target):  
    low=lower_no(nums,target)
    up=upper_no(nums,target)
    if low==-1 or nums[low]!=target:
        return f'No occurance of {target}'
    return f'target:{target} occurance-->{up+1-low}'
print(find_occur(nums,5))
