from Linked_List import Linked_list,node

if __name__ == '__main__':

    ll = Linked_list()

    # Create nodes using your node class
    n1 = node(1)
    n2 = node(2)
    n3 = node(3)
    n4 = node(4)
    n5 = node(5)
    n6 = node(6)
    n7 = node(7)
    n8 = node(8)
    n9 = node(9)

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

    n9.next = n3
def cyclde_detection_node(ll):
    s=ll.head
    f=ll.head
    while f is not None and f.next is not None:
        s=s.next
        f=f.next.next
        if s==f:
            s=ll.head
            while s!=f:
                s=s.next
                f=f.next
            return s.value
    return None
print(cyclde_detection_node(ll)) 
    