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

def find_middle(ll):
    s = ll.head
    if s is None:
        return None

    f = s.next

    while f.next is not None:
        s = s.next
        f = f.next.next

    return s.value
print(find_middle(ll))