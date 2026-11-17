def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        num=2**(n)
        result=[]
        for num in range(0,num):
            sub=[]
            for i in range(0,n):
                if num &(1<<i)!=0:
                    sub.append(nums[i])
            result.append(sub)
        return result