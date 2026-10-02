class Dictionary:
    def __init__(self,size):
        self.size=size
        self.n=0
        self.slot=[None]*self.size
        self.data=[None]*self.size
    
    def put(self,key,value):
        hash_value=self.hash_function(key)
        if self.slot[hash_value]==None:
            self.slot[hash_value]=key
            self.data[hash_value]=value
            self.n+=1
        
        else:
            if self.slot[hash_value]==key:
                self.data[hash_value]=value
            else:
                new_hash=self.__rehash(hash_value)
                
                while self.slot[new_hash]!=None and self.slot[new_hash]!=key:
                    if self.size==self.n:
                       self.resize_dict()
                       return self.put(key,value)
                    new_hash=self.__rehash(new_hash)
                
                if self.slot[new_hash]==None:
                    self.slot[new_hash]=key
                    self.data[new_hash]=value
                    self.n+=1
                
                elif self.slot[new_hash]==key:
                    self.data[new_hash]=value


                  

    def display_all (self):
        for i in range(self.size):
            print(f'{self.slot[i]}:{self.data[i]}',end='-- ')

    def resize_dict(self):
        self.slot=self.slot+[None]*self.size
        self.data=self.data+[None]*self.size
        self.size=self.size*2
    
    def hash_function(self,key):
       return abs(hash(key))%(self.size)
    
    def __rehash(self,old_hash):
        return (old_hash+1)%self.size
    
    def find_value(self,key):
        hash_value=self.hash_function(key)
        start_hash=self.hash_function(key)
        while self.slot[hash_value]!=None:
            if self.slot[hash_value]==key:
                return self.data[hash_value]
            hash_value=self.__rehash(hash_value)
            if hash_value==start_hash:
                return  f'{key} not found'
        return f'{key} not found'


       
    def _delete(self,key):
        hash_value=self.hash_function(key)
        for i in range(self.size):
            if self.slot[hash_value]==key:
                self.slot[hash_value]=None
                self.data[hash_value]=None
                return f'{key} Deleted'
            hash_value=self.__rehash(hash_value)
        return 'Doesnot exist key'

        

           




d=Dictionary(5)
d.put('pytho',25)
d.put('python',33)
d.put('prabaht',25)
d.put('mandira','mainali')


print(d.find_value(None))
# print(d._delete('khate'))
d.display_all()



