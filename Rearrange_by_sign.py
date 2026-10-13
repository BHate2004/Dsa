num=[5,12,10, 6, -3, -1, -10,-15]
def sign_change(num):
    second_array=[0]*len(num)
    p=1
    n=0
    for i in range(len(num)):
        if num[i]>0 and i==0:
            p=0
            n=1
        if num[i]>0 and  p<=len(num):
            second_array[p]=num[i]
            p+=2
        else:
            second_array[n]=num[i]
            n+=2
    return second_array



print(sign_change(num))
