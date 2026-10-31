nnn=5439025
# count=0
# while num>0:
#     count+=1
#     num=num//10
# print(count)

from math import log10,sqrt
# print(int(log10(num)+1))

# def _check_palindrome(num):
#     n=num
#     result=0
#     while n>0:
#         ld=n%10
#         result=(result*10)+ld
#         n=n//10
#     return result==num

# print(_check_palindrome(101))

# def _armstrong(num):
#     n=num
#     len=int(log10(n)+1)
#     sum_up=0
#     while n>0:
#         ld=n%10
#         sum_up+=ld**len
#         n=n//10
#     return sum_up==num

# print(_armstrong(153))

# def _find_factors(num):
#     lst=[]
#     for i in range(1,int(sqrt(36))+1):
#         if num%i==0 and num%i not in lst :
#             lst.append(i)
#         if num//i!=i and num%i==0 and num//i not in lst:
#             lst.append(num//i)
#     return  lst
# print(_find_factors(30))

# nums = [5, 6, 7, 7, 1, 9, 11, 1, 1, 5, 1, 1]
def _frequency_map(nums):
    fq_map={}
    for i in nums:
        if i not in fq_map:
            fq_map[i]=1
        else:
            fq_map[i]+=1
    return fq_map
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 11, 1, 4, 5, 6, 2]

def get_next_dict_count(n,m):
    get_count_dict=_frequency_map(n)
    check_dict={}
    for i in m:
        get_count_dict.get(i)
        if get_count_dict.get(i) is not None:
            check_dict[i]=get_count_dict.get(i)
        else:
            check_dict[i]=0
    return check_dict
print(get_next_dict_count(n,m))

