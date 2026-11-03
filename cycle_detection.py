from Linked_List import Linked_list,node

if __name__ == '__main__':

    ll = Linked_list()

    # Create nodes using your node class
    n1 = node(5)
    n2 = node(9)
    n3 = node(1)
    n4 = node(7)
    n5 = node(6)
    n6 = node(1)
    n7 = node(9)
    n8 = node(2)
    n9 = node(8)

    # Connect the nodes
    ll.head = n1

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9

    # n9.next = n3

# print(ll)
def detect_cycle(ll):
    new=set()
    current=ll.head
    while current!=None:
        if id(current) in new:
            return True
        new.add(id(current))
        current=current.next
    return False
print(detect_cycle(ll))

# better approach
def detect_cycle_best(ll):
    s=ll.head
    f=ll.head
    while f is not None and f.next is not None:
        s=s.next
        f=f.next.next
        if f==s:
            return True
    return False
print(detect_cycle(ll))