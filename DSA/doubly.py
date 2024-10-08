class Node:
    
    def __init__(self,data=None,pre=None,next=None):
        self.pre =pre
        self.data =data
        self.next =next

class doubly_ll:
    
    def __init__(self,head =None):
        self.head =head
    
   
    def traverse_from_front(self):
        temp =self.head
        if self.head is None:
            print("doubly inked list is empty")
        else:
            while temp is not None:
                print(temp.data,end ='<--->')
                temp =temp.next
            print(None)
    
    def traverse_from_back(self):
        temp =self.head
        if self.head is None:
            print("doubly linked list is empty")
        else:
            while temp.next is not None:
                temp =temp.next
            while temp is not None:
                print(temp.data,end ='<--->')
                temp =temp.pre
            print(None)
    
    def insertion_at_beginning(self,data):
        n =Node(data)
        temp =self.head
        if self.head is not None:
            n.next =self.head
            self.head.pre =n
        self.head=n
        n.pre =None
    
    def insert_at_end(self,data):
        n =Node(data)
        temp =self.head
        if self.head is not None:
            while temp.next is not None:
                temp =temp.next
            temp.next =n
            n.pre =temp
        else:
            self.head =n
    
    def del_at_beginning(self):
        temp =self.head
        if self.head is None:
            print("the doubelly lined list is empty")
            return
        
        if self.head.next is None:
            self.head =None
        else:
            self.head =temp.next
            self.head.pre =None
    
    def del_at_end(self):
    
        if self.head is None:
            print("list is already empty")
            return
        
        elif self.head.next is None:
            self.head =None
        
        else:
            pre =self.head
            temp =self.head.next
            
            while temp.next is not None:
                temp =temp.next
                pre =pre.next
            pre.next =None
    def insert_at_specified(self,data,position):
        n =Node(data)
        
        if self.head is None:
            if position==1:
                self.head =n
            
            else:
                print("the position in list do not exist and it can take only at 1st position")
            return
        
        if self.head.next is None:
            if position==1:
                n.next =self.head
                n.pre =None
                self.head.pre =n
                self.head =n
                
            return
        
        else:
            temp =self.head
            for i in range(position-2):
                if temp is None:
                    print("The position is beyond the current list length.")
                    return
                temp =temp.next
            n.next =temp.next
            n.pre =temp
            temp.next =n
    def del_at_specific(self,position):
            
        if position==1:
            if self.head is  None:
                print("the list  is already empty")
                return
            if self.head.next is None:
                self.head =None
                return
        else:
            temp =self.head.next
            prev =self.head
            for i in range(position-2):
                if temp is None:
                    print("the position is out of range")
                    return
                temp =temp.next
                prev =prev.next
            prev.next =temp.next
            temp.next.pre =prev

    def del_specific_item(self,data):
        temp =self.head
        if self.head is None:
            print("no such item to delete")
            return
        else:
            temp=self.head
            while temp is not None:
                if temp.data==data:
                    if temp.next is not None:
                        temp.next.pre=temp.pre
                    if temp.pre is not None:
                        temp.pre.next =temp.next
                    else:
                         self.head =temp.next
                    break
                temp =temp.next
            else:
                print("did not found item")
    def __iter__(self):
        return iterator(self.head)
        



class iterator:
    def __init__(self,head):
        self.current =head
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data =self.current.data
        self.current =self.current.next
        return data
        


    



# Create nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Initialize doubly linked list and link the nodes
dll = doubly_ll()
dll.head = n1
n1.next = n2
n2.pre = n1
n2.next = n3
n3.pre = n2
n3.next = n4
n4.pre = n3
n4.next = n5
n5.pre = n4

# Traverse from front
dll.traverse_from_front()

# #Traverse from back
dll.traverse_from_back() 
dll.del_at_beginning()
dll.del_at_end()
dll.traverse_from_front()
 
dll.insert_at_specified(position=3,data=6)
dll.traverse_from_front()
dll.del_at_specific(3)
dll.traverse_from_front()
dll.del_specific_item(4)
dll.traverse_from_front()


for i in dll:
    print(i,end=' ')
