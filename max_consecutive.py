
num= [1,102,99, 10, 98, 2,100, 5, 3,0]
def all_num(num):
   nums=set()
   for i in num:
      nums.add(i)
   return nums
# print(all_num(num))

def consecutive_length(num):
   max_lenght=0
   nums=all_num(num)
   for i in num:
      if i -1 not in nums:
         current=i
         count=1
         while current+1 in nums:
            count+=1
            current+=1
         if count>max_lenght:
            max_lenght=count
            count=0
   return max_lenght
print(consecutive_length(num))
            