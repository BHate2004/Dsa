def count_path(num):
    if num==0 or num==1:
        return 1
    return count_path(num-2)+count_path(num-1)
print(count_path(4))