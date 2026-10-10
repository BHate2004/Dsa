nums = [5, 9, 1, 2, 4, 15, 6, 3]
def find_two_sum(num,target):
    hash_map={}
    for i in range(len(num)):
        if not num[i] in hash_map:
            hash_map[num[i]]=i
    
    for i in range(len(nums)):
        remains=target-num[i]
        if remains in hash_map:
            return i,hash_map[remains]
    return 'not_found'
print(find_two_sum(nums,6))