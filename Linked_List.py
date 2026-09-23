class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Linked_list:
    def __init__(self):
        self.head=None
        self.num=0
        self.num=0
    def append_(self,value):
        new_node=node(value)
        if self.head==None:
            self.head=new_node
            self.num+=1
            return ''
        current_node=self.head
        while current_node.next!=None:
            current_node=current_node.next
        current_node.next=new_node
        self.num+=1

    def head_insert(self,value):
        new_node=node(value)
        if self.head==None:
            self.head=new_node
            self.num+=1
            return ''
        head=self.head
        self.head=new_node
        self.head.next=head
        self.num+=1

    def __str__(self):
        result=''
        current_node=self.head
        while current_node !=None:
            result+=str(current_node.value)+'-->'
            current_node=current_node.next
        return result[:-3]
    
    def _insert_middle(self,index,value):
        new_node=node(value)

        if index>=self.num:
            return self.append_(value)
        if self.head==None:
            self.head=new_node
            self.num+=1
            return ''
        if index<0:
            return 'Out of index'
        elif index==0:
            return self.head_insert(value)        
        current_node=self.head
        pos=0
        while pos!=index-1:
            current_node=current_node.next
            pos+=1
        next_node=current_node.next
        current_node.next=new_node
        current_node.next.next=next_node
        self.num+=1   
    
    def __len__(self):
        return self.num
    def clear_(self):
        self.head.next=None
        self.head=None
        self.num=0
        return self.__str__()
    
    def _delete_head(self):
        head=self.head
        self.head=head.next
        self.num-=1
    
    def delete_tail(self):
        if self.head==None:
            return 'Empty_list'
        if self.num==1:
            return self._delete_head()
        current_node=self.head
        while current_node.next.next!=None:
            current_node=current_node.next
        current_node.next=None
        self.num-=1
    
    def find_index(self,value):
        current_node=self.head
        pos=0
        while current_node!=None:
            if current_node.value==value:
                return pos
            current_node=current_node.next
            pos+=1

    def del_value(self,value):
        current_node=self.head
        if self.head==None:
            return 'empty list'
        if self.head.value==value:
            return self._delete_head()
        while current_node.next!=None:
            if current_node.next.value==value:
                next_val=current_node.next.next
                current_node.next=next_val
                return value
            current_node=current_node.next
        return 'not found'
    
    def search(self,value):
        if self.head==None:
            return 'Empty list'
        current_node=self.head
        while current_node!=None:
            if current_node.value==value:
                return current_node.value
            current_node=current_node.next
        return 'not found'
    def _reverse(self):
        prev=None
        current_node=self.head
        while current_node is not None:
            next_node=current_node.next 
            current_node.next=prev 
            prev=current_node 
            current_node=next_node 
        self.head=prev
    def reverse(self,node):
        if node is None:
            return 
        self.reverse(node.next)
        print(node.value,end=',')


l=Linked_list()
l.append_(10)
l.append_(20)
l.head_insert(52)
l.append_(50)
l.append_(500)
print(l)
print('______')
l.reverse(l.head)

1--2--3--4--5
