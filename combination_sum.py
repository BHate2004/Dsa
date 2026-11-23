results=[]
def combination_sum(target,nums, index,total=0,subets=[]):
    if index>=len(nums):
        return
    elif total==target:
        results.append(subets.copy())
        return
    elif total>target :
        return
    subets.append(nums[index])
    total+=nums[index]
    combination_sum(target,nums,index,total=total,subets=subets)
    subets.pop()
    total-=nums[index]
    combination_sum(target,nums,index+1,total=total,subets=subets)
combination_sum(7,[2,3,4],0)
print(results)