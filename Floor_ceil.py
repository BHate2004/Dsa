nums=[1,2,2,3,4,4,8,8,14,15]
def find_lower_bound(nums,target,low=0,high=len(nums)-1,lower_index=-1,mid=None,higher_index=-1):
    if low>high:
        if not nums[lower_index]<target:
            return [-1,nums[higher_index]]
        elif not nums[higher_index]>target:
            return [nums[lower_index],-1]

        return [nums[lower_index],nums[higher_index]]

    mid=(low+high)//2
    if nums[mid]==target:
        return [nums[mid],nums[mid]]
    elif nums[mid]>target:
        return find_lower_bound(nums,target,low=low,high=mid-1,lower_index=lower_index,mid=mid,higher_index=mid)
    elif nums[mid]<target:
        return find_lower_bound(nums,target,low=mid+1,high=high,lower_index=mid,mid=mid,higher_index=higher_index)
    
print(find_lower_bound(nums,5))