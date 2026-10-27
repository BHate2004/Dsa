nums=[1,2,3,4,5,9]
def find_lower_bound(nums,target,low=0,high=len(nums)-1,lower_index=-1,mid=None):
    

    if low>high:
        return f'insertion postition of {target}-->{lower_index}'
    mid=(low+high)//2
    if nums[mid]>=target:
        lower_index=mid
        return find_lower_bound(nums,target,low=low,high=mid-1,lower_index=lower_index,mid=mid)
    elif nums[mid]<target:
        return find_lower_bound(nums,target,low=mid+1,high=high,lower_index=lower_index,mid=mid)

print(find_lower_bound(nums,7))

