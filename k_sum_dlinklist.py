from doubly_link_list import double_linklist,_node
ll=double_linklist()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(6)
ll.append(8)
ll.append(9)
print(ll)

def _find_k_sum(ll,target):
    all_nodes=set()
    left=ll.head
    right=ll.tail
    while   left.value<right.value:
        total=left.value+right.value
        if total==target:
            if left.value<right.value:
                all_nodes.add(tuple((left.value,right.value)))
            else:
                all_nodes.add(tuple((right.value,left.value)))

            left=left.next
            right=right.prev
        elif total>target:
            right=right.prev
        else:
            if total<target:
                left=left.next
    
    return all_nodes 
print(_find_k_sum(ll,3))