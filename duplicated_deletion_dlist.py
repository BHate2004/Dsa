from doubly_link_list import double_linklist,_node
ll=double_linklist()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(4)



def remvoe_duplicates(ll):

    current=ll.head
    while current!=None:
        if current.next==None:
            return ll
        prev=current.prev

        while current.value==current.next.value:
            current=current.next
            if current.next==None:
                break
        if prev==None:
            ll.head=current
            current.prev=prev
            current=current.next
            continue
        prev.next=current
        current.prev=prev
        current=current.next
    return ll
print(ll)
print(remvoe_duplicates(ll))
print(f'head:{ll.head.value}')
print(f'tail:{ll.tail.value}')