def check_sub_sum(nums,target,index,total=0,subsets=[]):
    if total==target:
        return True
    elif index>=len(nums):
        return False
    
    else:
        if total>target:
            return False
    subsets.append(nums[index])
    total+=nums[index]
    check=check_sub_sum(nums,target,index=index+1,total=total,subsets=[])
    if check==True:
        return True
    subsets.pop()
    total-=nums[index]
    np=check_sub_sum(nums,target,index=index+1,total=total,subsets=[])
    return np
print(check_sub_sum([4,3,1],9,0))
