letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
nums='46'
 
result=[]
def lette_combination(nums,index,subsets=[]):
    if index>=len(nums):
        result.append(subsets.copy())
        return
    for let in letters[nums[index]]:
        subsets.append(let)
        lette_combination(nums,index+1,subsets)
        subsets.pop()

lette_combination(nums,0)

