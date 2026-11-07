def convert_binary(nums):
    result=''
    while nums>0:
        if nums%2==1:
            result+='1'
        else:
            result+='0'
        nums=nums//2
    return result[::-1]
print(convert_binary(9))