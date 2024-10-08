class Node:
   
    def __init__(self,data=None,next =None):
        self.data =data
        self.next =next
class Stack:
     
    def __init__(self,start=None,item_count=0):
        self.start =start 
        self.count_item =item_count

    def is_empty(self):
        return  self.start is None
    
    def push(self,data):
        n =Node(data)
        if self.start is None:
            self.start =n
            self.count_item+=1
        else:
            n.next =self.start
            self.start =n
            self.count_item+=1
    
    def pop(self):
        if self.start is None:
            raise Exception("no element to pop")
        
        elif self.start.next is None:
            print(self.start)
            self.start=None
        else:
            data=self.start.data
            self.start =self.start.next
        self.count_item-=1
        return data

    def peek(self):
        if self.start is not None:
            return self.start.data
        else:
            raise Exception("list is empty")
        
    def size(self):
        return self.count_item
        
    
    
s1 =Stack()
s1.start
s1.push(data=1)
s1.push(data=2)
s1.push(data=3)
s1.push(data=4)
s1.push(data=5)
s1.push(data=6)
s1.push(data=8)
s1.push(data=9)
s1.push(data=10)
s1.push(data=11)
s1.push(data=12)
print(s1.pop())
print(s1.size())
print(s1.peek())

