from typing import Any


class Node:
    def __init__(self,data=None,next=None,pre=None):
        self.data =data
        self.pre =pre
        self.next =next

class Deque:
    def __init__(self,front=None,rear=None):
        self.front =front
        self.rear =rear
        self.count_item =0
    
    def is_empty(self):
        return self.front is None
    
    def insert_front(self,data):
        n =Node(data)
        if self.is_empty():
            self.front =n
            self.rear =n
            n.next =None
            n.pre =None
        else: 
            if not self.is_empty():
                n.next =self.front
                self.front.pre =n
                self.front =n
                n.pre=None 
        self.count_item+=1 
    
    def del_at_front(self):
        if self.is_empty():
            raise Exception("the item cant be deleted as it is empty")
        
        elif self.front.next is None:
            self.front =None
        
        else:
            self.front=self.front.next
            self.front.pre =None
        
        self.count_item-=1
    
    def del_rear(self):
        if self.is_empty():
            raise Exception("no element to delete from the list")
        elif self.front.next is None:
            self.front=None
        else:
            self.rear=self.rear.pre
            self.rear.next =None
        self.count_item-=1

    def insert_at_rear(self,data):
        n =Node(data)
        if self.is_empty():
            self.front=n
            self.rear =n
        else:
            self.rear.next=n
            n.pre =self.rear
            self.rear =n
        self.count_item+=1
    
    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise IndexError("the deque do not have any elements")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            raise Exception("the deque is empty")
    def size(self):
        return self.count_item
    
# Create a new Deque
deque = Deque()

# Insert elements at the front
deque.insert_front(10)
deque.insert_front(20)
print("Front:", deque.get_front())  # Should print 20
print("Rear:", deque.get_rear())    # Should print 10
print("Size:", deque.size())         # Should print 2

# Insert elements at the rear
deque.insert_at_rear(30)
deque.insert_at_rear(40)
print("Front:", deque.get_front())  # Should print 20
print("Rear:", deque.get_rear())    # Should print 40
print("Size:", deque.size())         # Should print 4

# Delete an element from the front
deque.del_at_front()
print("Front after deletion:", deque.get_front())  # Should print 10
print("Size:", deque.size())                        # Should print 3

# Delete an element from the rear
deque.del_rear()
print("Rear after deletion:", deque.get_rear())    # Should print 30
print("Size:", deque.size())                        # Should print 2
