def rev_string(text,n):
    if n==len(text)-1:
        return text[n]
    return rev_string(text,n+1)+text[n]

print(rev_string('prabhat',0))