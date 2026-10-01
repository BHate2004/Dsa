class node:
    def __init__(self,key,value):
        self.key=key
        self.next=None
        self.value=value

        
class Linked_list:
    def __init__(self):
        self.head=None
        self.num=0
        
    def append_(self,key,value):
        new_node=node(key,value)
        if self.head==None:
            self.head=new_node
            self.num+=1
            return ''
        current_node=self.head
        while current_node.next!=None:
            current_node=current_node.next
        current_node.next=new_node
        self.num+=1

    def show(self):
        _key=[]
        _value=[]
        current_node=self.head
        while current_node !=None:
            _key.append(current_node.key)
            _value.append(current_node.value)
            current_node=current_node.next
        return str(list(zip(_key,_value)))[1:-1]
    
    def __str__(self):
        result=''
        current_node=self.head
        while current_node !=None:
            result+=str(current_node.key)+'-->'+str(current_node.value)+ ' '
            current_node=current_node.next
        return result[:-1]
     
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
        return head.key
    
   
    def search(self,key):
        if self.head==None:
            return 'Empty list'
        current_node=self.head
        while current_node!=None:
            if current_node.key==key:
                return current_node.value
            current_node=current_node.next
        return 'not found'
    
    def reverse(self):
        prev=None
        current_node=self.head
        while current_node is not None:
            next_node=current_node.next 
            current_node.next=prev 
            prev=current_node 
            current_node=next_node 
        self.head=prev

    def del_key(self,key):
            current_node=self.head
            if self.head==None:
                return 'empty list'
            if self.head.key==key:
                return self._delete_head()
            while current_node.next!=None:
                if current_node.next.key==key:
                    next_val=current_node.next.next
                    current_node.next=next_val
                    return key
                current_node=current_node.next
            return 'not found'




class dictll:
    def __init__(self,capacity):
        self.capacity=capacity
        self._bucket=self.makel_larray(self.capacity)
        self.size=0

    def makel_larray(self,size):
        lst=[]
        for i in range(size):
            lst.append(Linked_list())
        return lst

    def has_function(self,key):
        return abs(hash(key))%self.capacity

    def __rehash(self,old_hash):
        return (old_hash+1)%self.capacity

    def put(self,key,value):

        if self._load_factor()>1.2:
            self.resize()
        
        hash_value=self.has_function(key)

        
        if self._bucket[hash_value].head==None:
            self._bucket[hash_value].append_(key,value)
            self.size+=1
            return 
        current_node=self._bucket[hash_value].head

        while current_node!=None:

            if current_node.key==key:
                current_node.value=value
                return 
            current_node=current_node.next

        self._bucket[hash_value].append_(key,value)
        self.size+=1

    def _load_factor(self):
        return (self.size/self.capacity)

    def resize(self):
        old=self._bucket
        self._bucket=self.makel_larray(self.capacity*2)
        self.capacity=self.capacity*2
        self.size=0
        for ll in old:
            current_node=ll.head
            while current_node!=None:
                hash_values=self.has_function(current_node.key)
                self._bucket[hash_values].append_(current_node.key,current_node.value)
                current_node=current_node.next
                self.size+=1

    def _search(self,key):
        hash_value=self.has_function(key)
        current_ll=self._bucket[hash_value]
        return current_ll.search(key)
    
    def _del(self,key):
        hash_value=self.has_function(key)
        current_ll=self._bucket[hash_value]
        val=current_ll.del_key(key)
        if val==key:
            self.size-=1
        return val

        

d=dictll(5)
d.put('prabhat',27)
d.put('mainli',37)
d.put('prab',227)
d.put('mai',337)
d.put('bhat',72)
d.put('mara',72222)

print(d._del('mainali'))
print(d.size)