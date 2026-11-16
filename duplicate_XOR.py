def singleNumber(self, nums):
        res=0
        for i in nums:
            res=res^i
        return res
singleNumber([4,1,2,1,2])