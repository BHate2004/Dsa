arr=[1,2,2,2,5,6,7,8,9,0,1]
def find_second_occur(arr,target,index=None,count=None):
    if count==2:
        return index-1
    if len(arr)==index:
        return 'Not found'
    if arr[index]==target:
        return (find_second_occur(arr,target,index=index+1,count=count+1))
    return (find_second_occur(arr,target,index=index+1,count=count))

print(find_second_occur(arr,1,index=0,count=0))