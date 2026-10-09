nums = [0,1,1,1,1, 1, 0, 1, 0, 1, 1,0,1,1,1,1,1]

def _count_max_ones(num):
    count=0
    max=0
    for i in range(len(num)):
        if num[i]==1:
            count+=1

        elif num[i]!=1:
            if count>=max:
                max=count
                count=0
            else:
                count=0
        if i==len(num)-1:
            if count>=max:
                max=count
                count=0
    return max
print(_count_max_ones(nums))    