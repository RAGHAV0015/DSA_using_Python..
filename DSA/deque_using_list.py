class Deque:
    def __init__(self):
        self.deque=[] 
    
    def is_empty(self):
        return len(self.deque)==0
    
    
    
    def insert_at_front(self,data):
        self.deque.insert(0,data)
    
    
    def inser_at_end(self,data):
        self.deque.append(data)
    
    
    def del_at_front(self):
        if not self.is_empty():
            self.deque.pop(0)
        else:
            raise Exception("the list is empty hence cant del")
    
    def del_at_rear(self):
        if not self.is_empty():
            self.deque.pop()
        else:
            raise IndexError("the index out of range")
    def get_front(self):
        if  not self.is_empty():
            return self.deque[0]
        else:
            raise Exception("the list is empty")
    def get_rear(self):
        if  not self.is_empty():
            return self.deque[-1]
        else:
            raise Exception("the list is empty")
    
    def size(self):
        return len(self.deque)
        

# Create an instance of the Deque class
dq = Deque()

# Check if the deque is empty
print("Is deque empty?", dq.is_empty())  # Should print True

# Insert elements at the front and rear
dq.insert_at_front(10)
dq.inser_at_end(20)
dq.insert_at_front(5)

# Current state of the deque
print("Deque after insertions:", dq.deque)  # Should print [5, 10, 20]

# Check the front and rear elements
print("Front element:", dq.get_front())  # Should print 5
print("Rear element:", dq.get_rear())    # Should print 20
print("Size of deque:", dq.size())        # Should print 3

# Delete front and rear elements
dq.del_at_front()
print("Deque after deleting front:", dq.deque)  # Should print [10, 20]
dq.del_at_rear()
print("Deque after deleting rear:", dq.deque)   # Should print [10]

# Check the front, rear, and size again
print("Front element after deletion:", dq.get_front())  # Should print 10
print("Size after deletion:", dq.size())                # Should print 1

# Attempt to delete from an empty deque
dq.del_at_front()  # Should leave the deque empty
print("Deque after deleting front again:", dq.deque)   # Should print []

# Check if the deque is empty
print("Is deque empty?", dq.is_empty())  # Should print True
