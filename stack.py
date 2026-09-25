class node:
    def __init__(self,value):
        self.value=value
        self.next=None


class stack:
    def __init__(self):
        self.head=None
        self.num=0

    def push(self,value):
        new_node=node(value)
        if self.head==None: 
            self.head=new_node
            self.num+=1
            return ''
        head=self.head
        self.head=new_node
        self.head.next=head
        self.num+=1
      
    def is_empty(self):
        return self.head==None
    def __str__(self):
        current_node=self.head
        result=''
        while current_node!=None:
            result+=str(current_node.value)+'-->'
            current_node=current_node.next
        return result[:-3]
    def pop(self):
        if self.head==None:
            return 'Empty stack'
        data=self.head.value
        self.head=self.head.next
        self.num-=1
        return data
    def peek(self):
        if self.head==None:
            return 'Empty stack'
        return self.head.value
    def rev(self,new_text):
        s=stack()
        for i in new_text:
            s.push(i)
        res=''
        while not s.is_empty():
            res+=s.pop()
        return res
 
