import ctypes

class list_:
    def __init__(self,size):
        self.size=size
        self.n=0
        self.A=self.__make_array(self.size*2)

    def append(self,value):
        if self.size==self.n:
            self.resize(self.size*2)
        self.A[self.n]=value
        self.n+=1
    def _pop(self):
        if self.n==0:
            return 'Empty list'
        print(self.A[self.n-1])
        self.n=self.n-1

    def __getitem__(self, index):
        if index>=self.n or index<0:
            return 'index out of bound'
        return self.A[index]
    def resize(self,new_capacity):
        B=self.__make_array(new_capacity)
        self.size=new_capacity
        for index in range(self.n):
            B[index]=self.A[index]
        self.A=B 
    def find(self,value):
        if self.n==0:
            return "Empty"
        for i in range(self.n):
            if self.A[i]==value:
                return i
        return 'Not found'

    def _insert(self,index,value):
        if self.n==self.size:
            self.resize(self.size*2)
        if index>=self.n:
            return 'too far form indexing'
        for i in range(self.n,index,-1):
            self.A[i]=self.A[i-1]
        self.A[index]=value
        self.n+=1

            

    def __make_array(Self,capacity):
        return (capacity*ctypes.py_object)()
    def __len__(self):
        return self.n
    def _clear(self):
        self.n=0
        self.size=1
    def __delitem__(self,pos):
        if 0<=pos<self.n:
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n-=1

    def _min(self):
        min=self.A[0]
        for i in range(self.n):
            if self.A[i]<min:
                min=self.A[i]
        return min
    def _max(self):
        max=self.A[0]
        for i in range(self.n):
            if self.A[i]>max:
                max=self.A[i]
        return max
    
    def _remove(self,value):
        index=self.find(value)
        self.__delitem__(index)
    def __str__(self):
        result=''
        for i in range(self.n):
            result+=str(self.A[i])+','
        return '['+result[:-1]+']'
    def _extend(self,new_obj):
        if self.n==self.size:
            self.resize(2*self.size)
        running_index=0
        start_index=self.n
        end_index=self.n+len(new_obj)
        for i in range(start_index,end_index):
            self.A[i]=new_obj[running_index]
            if running_index!=len(new_obj)-1:
                running_index+=1
            self.n+=1
    def _slicing(self,start=None,end=None):
        if start==None and end==None:
            return self.__str__()
        result=''
        for i in range(start,end):
            result+=str(self.A[i])+','
        return '['+result[:-1]+']'

    def __add__(self,new_obj):
        self._extend(new_obj)
        return self.__str__()
        


l=list_(5)
l.append(4)
l.append(15)
l.append(12)
l.append(52)
print(l._min())
print(l._slicing(0,3))
b=list_(5)
b.append(10)
b