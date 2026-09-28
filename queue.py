from stack import stack
class queque():
    def __init__(self):
        self.enqu=stack()
        self.deque=stack()
    def enq(self,value):
        self.enqu.push(value)

    def deq(self):
        if self.enqu.is_empty() and self.deque.is_empty():
           print('The list is empty')
           return 'The list is empty'
        if self.deque.is_empty():
            while not self.enqu.is_empty():
                self.deque.push(self.enqu.pop())
        return self.deque.pop() 
            
    def __allenque(self):
        new_result=''
        current_node=self.enqu.head
        while current_node!=None:
                new_result=str(current_node.value)+'-'+new_result
                current_node=current_node.next
        return new_result[:-1]
    def __alldeque(self):
            result=''
            current=self.deque.head
            while current!=None:
                result+=str(current.value)+'-'
                current=current.next
            return result[:-1]
     
    def __str__(self):
        if self.enqu.is_empty() and self.deque.is_empty():
            return 'Empty list'
        elif self.deque.is_empty() and not self.enqu.is_empty():
             return self.__allenque()
        elif not self.deque.is_empty() and self.enqu.is_empty():
             return self.__alldeque()
        else:
             return self.__alldeque()+self.__allenque()
        
s=queque()
s.enq(5)
s.enq(10)
s.enq(20)
s.enq(40)
s.enq(500)
s.deq()
s.deq()

print(s)