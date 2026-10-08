num=[9, 6, 4, 2, 3, 5, 7, 0, 1]
def find_missing(num,count=0):
    if count==len(num):
        return count
    sum_up=count+find_missing(num,count+1)
    if count==0:
        return sum_up-sum(num)
    return sum_up
print(find_missing(num))
    