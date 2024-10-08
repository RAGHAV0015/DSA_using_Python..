class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            raise IndexError("list is empty")
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("the list is empty")
    
    def size(self):
        return len(self)
    # implement a way to restrict use of insert() methord of list calss from stack object
    
    def insert(self,index,data):
        raise AttributeError("No Attribute 'insert' in the stack class")
    


        

    

