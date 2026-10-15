def reverse_arr(num):
    left=0
    right=len(num)-1
    while left<right:
        left_num=num[left]
        right_num=num[right]
        num[right]=left_num
        num[left]=right_num
        left+=1
        right-=1
    return num
print(reverse_arr([2,4,6,70,7]))
[5,7,3,8,9]