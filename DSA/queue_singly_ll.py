class Node:
    def __init__(self,data=None,next=None):
        self.data =data
        self.next =next
class Queue:
    
    def __init__(self,front=None,rear=None):
        self.front =front
        self.rear =rear
        self.count =0
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self,data):
        n =Node(data)
        if self.is_empty():
            self.front=n
            self.rear =n
            n.next =None
        else:
            self.rear.next =n
            self.rear =n
        self.count+=1
    def dequeue(self):
        if self.is_empty():
            raise Exception("no element to deque as empty queue")
        elif self.front.next is None:
            self.front =None
            self.rear =None
        else:
            self.front=self.front.next
        self.count-=1

    def get_front(self):
        if self.is_empty():
            raise Exception("the que is empty to fetch")
        else:
            return self.front.data
    def get_rear(self):
        if self.is_empty():
            raise Exception("the list is empty hence cant be fetched")
        else:
            return self.rear.data
    def size(self):
        if not self.is_empty():
            return self.count    


q1 =Queue()
q1.enqueue(1)
q1.enqueue(13)
q1.enqueue(14)
q1.enqueue(31)
q1.enqueue(15)
q1.enqueue(17)
q1.enqueue(19)
q1.enqueue(21)
q1.enqueue(111)
print(q1.get_front(),q1.get_rear())
print(q1.size())
q1.dequeue()
print(q1.get_front())
q1.dequeue()
q1.dequeue()
q1.dequeue()
print(q1.get_front())

