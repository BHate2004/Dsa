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
    n9.next=None

def find_odd_pos(ll):
    current=ll.head
    odd_head=None
    prev_odd=None
    even_head=None
    prev_even=None
    count=1
    while current!=None:
        if count%2!=0:
            if prev_odd is None and odd_head is None:
                prev_odd=current
                odd_head=current
                count+=1
                current=current.next
                continue
            prev_odd.next=current
            prev_odd=current

        elif count%2==0:
            if even_head is None and prev_even is None:
                prev_even=current
                even_head=current
                count+=1
                current=current.next
                continue
            prev_even.next=current
            prev_even=current
        count+=1
        current=current.next
    prev_odd.next=None
    prev_even.next=None
    return odd_head,even_head
odd,even=find_odd_pos(ll)
cur=odd
def change_position(odd,even):
    ev=even
    od=odd
    cur=od
    while cur.next!=None:
        cur=cur.next
    cur.next=ev
    current=odd
    while current!=None:
        print(current.value)
        current=current.next

            
                
change_position(odd,even)
        



