nums = [4, 5, 6, 7, 0, 1, 2]
def find_min(nums,low=0,high=len(nums)-1,mid=None,min=None):
    if low>high:

        return min

    mid=(low+high)//2
    if min is None:
        min=nums[mid]
    if nums[mid]-nums[low]>=0:
    
            if nums[low]<min:
    
                return find_min(nums,low=mid+1,high=high,mid=mid,min=nums[low])
    
            return find_min(nums,low=mid+1,high=high,mid=mid,min=min)
    elif nums[high]-nums[mid]>=0:
        
        if  nums[mid]<min:

            return find_min(nums,low=low,high=mid-1,mid=mid,min=nums[mid])

        return find_min(nums,low=low,high=mid-1,mid=mid,min=min)
    

print(find_min(nums))