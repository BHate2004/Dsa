result=[]
def generate_pa(paran,index,total=0):
    if index>=len(paran):
        if total==0:
            result.append(''.join(paran.copy())) 
        return
    if total<0:
        return       
    elif total>len(paran)//2 or total==-1:
        return
    paran[index]='('
    sum=total+1
    generate_pa(paran=paran,index=index+1,total=sum)
    paran[index]=')'
    sum=total-1
    generate_pa(paran=paran,index=index+1,total=sum)
generate_pa(['']*4,0)
print(result)
