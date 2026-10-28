nums=[1,2,2,3,4,4,8,8,14,15]
def find_lower_bound(nums,target,low=0,high=len(nums)-1,mid=None,first=-1):
    if low>high:
        return  first
    mid=(low+high)//2
    if nums[mid]>=target:
        return find_lower_bound(nums,target,low=low,high=mid-1,mid=mid,first=mid)
    elif nums[mid]<target:
        return find_lower_bound(nums,target,low=mid+1,high=high,mid=mid,first=first)
# print(find_lower_bound(nums,4))



def find_higher_bound(nums,target,low=0,high=len(nums)-1,mid=None,last=-1):
    if low>high:
        return  last
    mid=(low+high)//2
    if nums[mid]<=target:
        return find_higher_bound(nums,target,low=mid+1,high=high,mid=mid,last=mid)
    elif nums[mid]>target:
        return find_higher_bound(nums,target,low=low,high=mid-1,mid=mid,last=last)
# print(find_higher_bound(nums,4))

def  low_up(num,target):
    a=[]
    a.append(find_lower_bound(nums,target))
    a.append(find_higher_bound(nums,target))
    return a
print(low_up(nums,4))
    

        
       
    


