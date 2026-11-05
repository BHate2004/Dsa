class _node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class double_linklist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.n=0

    def append(self,value):
        new_node=_node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.n+=1
            return 
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node
        self.n+=1


    def _insert(self,value):
        new_node=_node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            self.n+=1
            return
        next_node=self.head
        self.head=new_node
        self.head.next=next_node
        next_node.prev=self.head
        self.n+=1

    def insert_position(self,index,value):
        new_node=_node(value)
        if self.head==None or index==0:
            self._insert(value)
            return 
        if index<0:
            raise Exception('out of bound')
        if index>=self.n:
            return self.append(value)
        count=0
        curr=self.head
        while not count==index-1:
            curr=curr.next
            count+=1
        next_node=curr.next
        next_node.prev=new_node
        new_node.prev=curr
        curr.next=new_node
        new_node.next=new_node
        self.n+=1


    def delete_head(self):
        if self.head==None:
            return 'Empty'
        if self.n==1:
            self.head=None
            self.tail=None
            self.n-=1
            return
        next_head=self.head.next
        self.head=next_head
        self.head.prev=None
        self.n-=1

    def delete_tail(self):
        if self.tail==None:
            return 'Empty'
        if self.n==1:
            self.head=None
            self.tail=None
            self.n-=1
            return 
        prev_node=self.tail.prev
        self.tail=prev_node
        self.tail.next=None
        self.n-=1

    def __str__(self):
        result=''
        result_=''
        curr=self.head
        while curr!=None:
            result+=str(curr.value)+'-->'
            curr=curr.next
       

        
        return result+str(None)


    def _reverse_(self):
        if self.head==None:
            raise Exception('cant reverse empty list')
        curr=self.head
        next=None
        while curr.next!=None:
            if next is None:
                self.tail=curr
            next_node=curr.next
            curr.next=next
            next=curr
            curr.prev=next_node
            curr=next_node
        self.head=curr
        curr.next=next
        curr.prev=None
            
    def _del_val(self,value):
        if self.head==None:
            return 'empty'
        current=self.head
        while current!=None:
            if current==self.head and current.value==value:
                self.delete_head()
                current=current.next
                continue
            if current.value==value:
                total=0
                prev_node=current.prev
                while current!=None and current.value==value:
                    total+=1
                    current=current.next
                self.n-=total
                if self.n==0:
                    self.head=None
                    self.tail=None
                    return 'empty'
                if current==None:
                    prev_node.next=None
                    self.tail=prev_node
                else:
                    prev_node.next=current
                    current.prev=prev_node
                    current=current.next
                
            else:
                current=current.next
            


ll = double_linklist()


ll.append(0)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll._insert(2)


print(ll.n)
ll._del_val(2)
print(ll)
ll._reverse_()
print(ll)

