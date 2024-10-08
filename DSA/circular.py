class Node:
    def __init__(self,data=None,next=None):
        self.data =data
        self.next =next

class circular_ll:
    
    def __init__(self,last=None):
        self.last =last
    
    
    
    def is_empty(self):
        return self.last is None
    
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.last is not None:
            n.next =self.last.next
            self.last.next =n
        elif self.last is None:
            self.last =n
            n.next =n
        #If self.last.next is None, it would indicate a broken circular structure, which should not happen in a well-maintained circular linked list.
    def insert_at_last(self,data):
        n =Node(data)
        if self.last is not None:
            n.next =self.last.next
            self.last.next =n
            self.last =n
        elif self.last is None:
            self.last =n
            n.next =n 
    
    def search(self,data):
        if self.last is None:
            print("no element to search")
            return
        if self.last is not None:
            temp =self.last.next
            while True:
                if temp.data==data:
                    return data
                temp =temp.next
                if temp==self.last.next:
                    break
            return "the element not found"

    def insert_after_given_node(self,data,position):
        n =Node(data)
        
        if position==1:
            if self.last is None:
                self.last =n
                n.next =n
            else:
                n.next =self.last.next
                self.last.next =n
            return
        
        if self.last is not None:
            temp =self.last.next
            for i in range(position-1):
                temp=temp.next
                if temp ==self.last:
                    print("the position is out of range")
                    return       
            n.next =temp.next
            temp.next =n

    def del_at_first(self):
        if self.last is None:
            print("list is already empty")
            return
        
        
        if self.last.next ==self.last:
            self.last= None
        else:
            self.last.next=self.last.next.next
            
    def del_at_end(self):
        if self.last is None:
            print("nothing to delete")
            return
        elif self.last.next==self.last:
            self.last=None
        else:
            temp =self.last.next
            while True:
                if temp.next ==self.last:
                    temp.next=self.last.next
                    self.last =temp
                    break
                temp=temp.next
    
    def del_at_specific(self,data,position):
        if self.last is None:
            print("noelement to delete")
            return
        elif position==1:
            if self.last==self.last.next:
                self.last =None
            else:
                self.last.next =self.last.next.next
                return
        else:
            temp=self.last.next
            for i in range(position-2):
                temp=temp.next
                if temp==self.last.next:
                    print("position is out of range")
                    return
            temp.next =temp.next.next
            if temp.next==self.last.next:
                self.last=temp
    
    def traverse(self):
        if self.last is None:
            print("the list is empty")
            return
        
        else:
            temp =self.last.next
            while True:
                print(temp.data,end=' ')
                temp =temp.next
                if temp==self.last.next:
                    break
            print()
   
    def __iter__(self):
        return iterator(self.last)               




class iterator:
    def __init__(self,last):
        self.current =last
        self.last=last
    def __iter__(self):
        return self
    def __next__(self):
        if self.last is None  or self.current == self.last.next:
            raise StopIteration
        data =self.last.data
        self.last=self.last.next
        return data



                


n1 =Node(data=1)
n2=Node(data=2)
n3=Node(data=3)
n4=Node(data=4)
n5=Node(data=5)

# Create a circular linked list
cll = circular_ll()

# Insert elements at the start
cll.insert_at_start(1)
cll.insert_at_start(2)
cll.insert_at_start(3)

# Traverse and print the list
print("List after inserting at start:")
cll.traverse()  # Output: 3 2 1

# Insert elements at the last
cll.insert_at_last(4)
cll.insert_at_last(5)

# Traverse and print the list
print("\nList after inserting at last:")
cll.traverse()  # Output: 3 2 1 4 5

# Insert after a given node (e.g., after position 2)
cll.insert_after_given_node(10, 2)

# Traverse and print the list
print("\nList after inserting 10 after position 2:")
cll.traverse()  # Output: 3 10 2 1 4 5

# Delete the first element
cll.del_at_first()

# Traverse and print the list
print("\nList after deleting the first element:")
cll.traverse()  # Output: 10 2 1 4 5

# Delete the last element
cll.del_at_end()

# Traverse and print the list
print("\nList after deleting the last element:")
cll.traverse()  # Output: 10 2 1 4

# Delete a specific element (e.g., position 2)
cll.del_at_specific(2, 2)

# Traverse and print the list
print("\nList after deleting element at position 2:")
cll.traverse()  # Output: 10 1 4

for i in cll:
    print(i,end =' ')



    #--------------------------------------------------------------------------------------------------------------    
        
        #"""2nd methord to traverse the circular link list""
        
        # if self.last is not None:
        #     temp =self.last.next
        #     while temp is not self.last:
        #         temp =temp.next
    #-----------------------------------------------------------------------------------------------------------------        
        #this would be my 1st logic to traverse:
        
        # if self.last is not None:
        #     temp =self.last.next
        #     while True:
        #         print(temp.data)#this will print the first element of the list
        #         temp =temp.next
        #         if temp==self.last.next:
        #             break
    #---------------------------------------------------------------------------------------------------------------
    

        
            

    
      