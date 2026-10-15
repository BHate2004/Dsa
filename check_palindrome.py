def check_palindrome(text,l,r):
    if l>=r or r<=l:
        return True
    if text[l]!=text[r]:
        return False
    return check_palindrome(text,l+1,r-1)
print(check_palindrome('nitin',l=0,r=4))