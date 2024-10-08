class Stack:
    def __init__(self):
        self.stack =[]
    
    def is_empty(self):
        return len(self.stack)==0
    
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print("on item to pop")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[len(self.stack)-1]#return self.stack[-1]
        else:
            print("the stack is empty ")
    
    def size(self):
        if not self.is_empty():
            return len(self.stack)
        else:
            raise IndexError("the stack is empty")




s1 =Stack()
s1.push(10)
s1.push(11)
s1.push(22)
s1.push(55)
s1.push(60)
print(s1.peek())
s1.pop()
print(s1.peek())
    



