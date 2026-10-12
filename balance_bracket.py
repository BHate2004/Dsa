from stack import stack
brack='[{()}]'
def _find_balanced(txt):
    s=stack()
    new_lst=[')','}',"]"]
    check={'}':'{',')':'(',']':'['}
    for i in txt:
        if i not in new_lst:
            s.push(i)
    for text in txt:
        if text  in new_lst:
            if s.peek()!=check[text]:
                return 'Found_imbalanced'
            else:
                s.pop()
    return 'Found_balanced'
