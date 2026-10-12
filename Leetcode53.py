# num=[-2,1,-3,4,-1,2,-2,-5,4]
num = [-5, -2, -8, -1,8]
def _find(num):
    total=None
    max=0
    for i in range(len(num)):
        if total is None:
            total=num[i]
            max=num[i]
            continue
        total+=num[i]
        if total>max:
                max=total
        elif total<0:
            total=0
        
    return max
print(_find(num))