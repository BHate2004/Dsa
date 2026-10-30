num= [0, 1, 2, 10, 11, 12, 13, 14, 50, 51]
def find_min_max(num):
   min=num[0]
   max=num[0]
   all_nums={}
   for i in num:
      all_nums[i]=i
      if i<min:
         min=i
      if i>max:
         max=i
   return min,max,all_nums
