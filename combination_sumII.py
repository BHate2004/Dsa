results=[]
def combiantion_sumII(nums,target,index,total=0,subsets=[]):
    if total==0:
        results.append(subsets.copy())
        return 
    elif target<0:
        return
    elif index>len(nums):
        return 
    for i in range(index,len(nums)):
        if i>index and nums[i]==nums[i-1]:
            continue
        subsets.append(nums[i])
        sum_=total-nums[i]
        combiantion_sumII(nums,target,i+1,sum_,subsets)
        subsets.pop()
combiantion_sumII([1,1,1,2,2],4,0,4)
print(results)