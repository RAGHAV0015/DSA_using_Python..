class PriorityQueue:
    def __init__(self):
        self.items=[]
    
    def push(self,data,priority):
        index=0
        while len(self.items)>index and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    
    def is_empty(self):
        return len(self.items)==0
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            raise IndexError("the list queue is empty")
        
    def size(self):
        return len(self.items)


p1=PriorityQueue()
p1.push(23,0)
p1.push(34,-2)
p1.push(78,2)
p1.push(99,-2389)

print(p1.pop())



