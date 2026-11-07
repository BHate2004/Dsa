def decimal_(num:str):
    pow=0
    total=0
    for i in num[::-1]:
        total+= int(i)*2**pow
        pow+=1
    return total
print(decimal_('1011'))