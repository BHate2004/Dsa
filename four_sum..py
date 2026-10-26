ar = [3, 1, 5, 2, 4, 1, 3, 5, 2, 4, 1, 3]
def four_sum(ar):
    n=len(ar)
    all_set=set()
    unique_no=set()
    for i in range(n):
        all_set.add(ar[i])
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                result=8-(ar[i]+ar[j]+ar[k])
                if  result in all_set:
                    sort=sorted([ar[i],ar[j],ar[k],result])
                    unique_no.add(tuple(sort))
    return unique_no
print(four_sum(ar))









