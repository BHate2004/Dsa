result=[]
def k_sub(nums,target,index,subsets=[]):
    if index>=len(nums):
        if sum(subsets)==target:
            result.append(subsets.copy())
        return 
    subsets.append(nums[index])
    k_sub(nums,target,index=index+1,subsets=subsets)
    subsets.pop()
    k_sub(nums,target,index=index+1,subsets=subsets)
k_sub([5,9,4,3,4,1],9,0)
print(result)