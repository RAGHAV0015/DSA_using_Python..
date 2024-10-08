class Queue:
    def __init__(self):

        self.lists =[]
    
    def is_empty(self):
        return len(self.lists)==0
    
    def enqueue(self,data):
        self.lists.append(data)
    
    def dequeue(self):
        if not self. is_empty():
            self.lists.pop(0)
        else:
            raise IndexError("the element queue undeflow")

    def get_front(self):
        if not self.is_empty():
            return self.lists[0]
        else:
            raise IndexError("the queue is over flow")

    def get_rear(self):
        if not self.is_empty():
            return self.lists[-1]
        else:
            raise IndexError("the queue is empty")
    
    def size(self):
        return len(self.lists)
    
q1 =Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print(q1.get_front())
q1.dequeue() 
print(q1.get_front()) 
print(f"queue has now {q1.size()} elements")
    


