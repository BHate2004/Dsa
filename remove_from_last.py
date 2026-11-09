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
# print(_find_len(ll))

def _remove_from_last(ll,index):
    pos=_find_len(ll)-index
    current=ll.head
    count=0
    if pos<0 or index<0:
        return 'out of index'
    if pos==0:
        head=ll.head.next
        ll.head=head
        return ll 
    while count!=pos-2 and current!=None:
        count+=1
        current=current.next
    current.next=current.next.next
    return ll
print(_remove_from_last(ll,5))

