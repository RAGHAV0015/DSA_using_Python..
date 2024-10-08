from  link import Sll

class Stack:
    def __init__(self):
        self.mylist =Sll()
        self.item_count =0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    
    def pop(self):
        self.mylist.del_at_beginning()
        self.item_count-=1
    
    def peek(self):
        if self.mylist.is_empty():
            return "element cant be peeked as the list is empty"
        else:
            return self.mylist.head.data
    def size(self):
        return self.item_count



s =Stack()
s.push(10)
s.push(11)
s.push(15)
s.push(22)
s.push(72)
print(s.peek())




