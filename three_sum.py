ar=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
def find_three_sum(arr):
  
    arr=set()
    lst=set()
    for i in range(len(ar)):
        arr.add(ar[i])
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            find_value=-(ar[i]+ar[j])
            if find_value in arr:
                a=list([ar[i],ar[j],find_value])
                a=sorted(a)
                lst.add(tuple(a))
    return

print(sorted(ar))
# better approach
def  better_find_sum(ar):
    ans=set()
    ar.sort()
    n=len(ar)
    for i in range(n):
        if i!=0 and ar[i]==ar[i-1]:
            continue
        j=i+1
        k=n-1
        while j<k:
            if ar[i]+ar[j]+ar[k]==0:
                vals=list([ar[i],ar[j],ar[k]])
                ans.add(tuple(vals))
                j+=1
                k-=1
            elif ar[i]+ar[j]+ar[k]<0:
                j+=1
            else:
                k-=1
    return ans
print(better_find_sum(ar))