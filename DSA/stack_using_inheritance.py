from link import*

class Stack(Sll):
    def __init__(self):
        super().__init__()
        self.count_item =0
    
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.count_item+=1

    def pop(self):
        if not self.is_empty():
            data =self.start.data
            self.del_at_beginning()
            self.count_item-=1
            return data
        else:
            raise IndentationError("stack under flow")

    
    
    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndentationError("stack underflow")
    
    def seize(self):
        return self.count_item





s1 =Stack()
s1.push(11)
s1.push(12)
s1.push(10)
s1.push(20)
print("top element on the stack is ",s1.peek())
s1.pop()
print("top element on the stack is ",s1.peek())