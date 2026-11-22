results=[]
def allB_strings(nums,index,Flag):
    if index>=len(nums):
        results.append(''.join(nums))
        return
    nums[index]='0'
    allB_strings(nums=nums,index=index+1,Flag=True)
    if Flag==True:
        nums[index]='1'
        allB_strings(nums=nums,index=index+1,Flag=False)
    nums[index]='0'
allB_strings(['0']*3,0,True)
print(results)
    
