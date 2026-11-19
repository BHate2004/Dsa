result=[]
def sub_seq(nums,index,subsets=[]):
    if index>=len(nums):
        result.append(subsets.copy())
        return 
    subsets.append(nums[index])
    sub_seq(nums,index=index+1,subsets=subsets)
    subsets.pop()
    sub_seq(nums,index=index+1,subsets=subsets)
sub_seq([1,2,3],0)
print(len(result))
