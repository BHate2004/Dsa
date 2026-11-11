from Linked_List import Linked_list,node
ll=Linked_list()
ll.append_(5)
ll.append_(10)
ll.append_(20)
ll.append_(30)
ll.append_(40)
ll.append_(50)
ll.append_(60)

print(ll)

def find_len(ll):
    current=ll.head
    count=0
    while current!=None:
        current=current.next
        count+=1
    return count
# print(find_len(ll))

def find_middle(ll):
    if ll.head==None:
        return 'empty list'
    count=0
    current=ll.head
    while count!=find_len(ll)//2:
        count+=1
        current=current.next
    return current.value
print(find_middle(ll))
