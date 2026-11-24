result=[]
def subsets_sum(nums,index,subsets=[]):
    if index>=len(nums):
        result.append(sum(subsets.copy()))
        return 
    subsets.append(nums[index])
    subsets_sum(nums,index+1,subsets)
    subsets.pop()
    subsets_sum(nums,index+1,subsets)
subsets_sum([5, 6, 7],0)
print(result)