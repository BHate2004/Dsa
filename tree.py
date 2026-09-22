class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_tree:
    def  __init__(self):
        self.top_node=None
        self.n=0

    def _add_node(self,data):
        new_node=node(data)
        if self.top_node is None:
            self.top_node=new_node
            self.n+=1
        else:
            self._assign_node(self.top_node,data)
        
    
    def _assign_node(self,root_node,data):
        new_node=node(data)
       
        if new_node.data<root_node.data:
            if root_node.left is None:
                root_node.left=new_node
                return
            else:
                self._assign_node(root_node.left,data)
        elif new_node.data>root_node.data:
            if root_node.right is None:
                root_node.right=new_node
                return
            else:
                self._assign_node(root_node.right,data)

    def inOrderTraversal(self,node):
        if node is None:
            return

        self.inOrderTraversal(node.left)   
        print(node.data, end=", ")    
        self.inOrderTraversal(node.right)  
            
b=Binary_tree()
b._add_node(100)

b._add_node(50)
b._add_node(40)
b._add_node(60)
b._add_node(500)
b._add_node(10)
b._add_node(4)
b._add_node(250)
b._add_node(550)
b.inOrderTraversal(b.top_node)