def find_no(num,target,index):
    if len(num)==index:
        return 0
    count=1 if num[index]==target else 0
    return count+find_no(num,target,index+1)
print(find_no([1,2,3,1,2],2,index=0))

