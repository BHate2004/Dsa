nums= [14,14,14,15,16,10,11,11,12,13,14,14]


def search_no(nums,target,low=0,high=len(nums)-1,mid=None):
    if low>high:
        return -1
    mid=(low+high)//2
   
    if nums[mid]==target:
        return mid
    if nums[mid]==nums[low]==nums[high]:
        return search_no(nums,target,low=low+1,high=high-1)
    elif nums[high]-nums[mid]>=0:
        if nums[mid]<=target<=nums[high]:
            return search_no(nums,target,low=mid+1,high=high,mid=mid)
        else:
            return search_no(nums,target,low=low,high=mid-1,mid=mid)
    elif nums[mid]-nums[low]>=0:
        if nums[low]<=target<=nums[mid]:
            return search_no(nums,target,low=low,high=mid-1,mid=mid)
        else:
            return search_no(nums,target,low=mid+1,high=high,mid=mid)



        
            

print(search_no(nums,12))

    
