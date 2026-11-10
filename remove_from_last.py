from Linked_List import Linked_list,node
ll=Linked_list()
ll.append_(20)
ll.append_(30)
ll.append_(40)
ll.append_(50)
ll.append_(60)

def _find_len(ll):
    current=ll.head
    count=0
    while current!=None:
        count+=1
        current=current.next
    return count
def remove_form_last(ll,index):
    pos=_find_len(ll)-index-1
    count=0
    currrent=ll.head
    if not 0<=index<_find_len(ll):
        return 'out of index'
    
    if pos==0:
        ll.head=ll.head.next
        return ll
    while not count==pos-1:
        count+=1
        currrent=currrent.next
    currrent.next=currrent.next.next
    return ll
print(remove_form_last(ll,3))
    