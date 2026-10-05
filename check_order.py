def check_order(num,index=0):

    if len(num)-1==index:
        return index
    check_index=index
    return_value=check_order(num,index+1)
    if num[check_index]>num[return_value] or type(return_value) is not int:
        return False
    if index==0 and  num[check_index]<num[return_value]:
        return num
    if num[check_index]<num[return_value]:
        return check_index
    
print(check_order([1,2,4,9,8]))
