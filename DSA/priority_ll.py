class Node:
    def __init__(self,data=None,priority=None,next=None):
        self.data =data
        self.next =next
        self.priority =priority

class PriorityQueue:
    def __init__(self,head=None):
        self.head= head
        self.count_items =0
    
    def is_empty(self):
        return self.head is None

    def push(self,data,priority):
        n=Node(data,priority)
        if self.is_empty() or self.head.priority>priority:
            n.next =self.head
            self.head =n
        else:
            temp =self.head
            while temp.next is not None and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.count_items+=1

    def pop(self):
        if self.head is None:
            raise Exception("the list is empty and can't return ant element")
        elif self.head.next is None:
            self.count_items-=1
            return self.head.data
        else:
            temp =self.head
            self.head =temp.next
            self.count_items-=1
            temp.next =None
         
        return temp.data
    def size(self):
        return self.count_items 

p1 =PriorityQueue()
p1.push(23,2)
p1.push(52,0)
p1.push(23,-1)
p1.push(17,11)
print(p1.pop())
p1.pop()
p1.pop()
print(p1.pop())
print(p1.size())


    

    





