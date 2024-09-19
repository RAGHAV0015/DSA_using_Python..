class Node:
    def __init__(self,data=None,next=None):
        self.data =data
        self.next =next
class Sll:
    def __init__(self,start=None):
        self.start =start
    
    def is_enpty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n =Node(data)
        n.next =self.start#assigning the reference that is present in self.head to n.next so to could connect from right first
        self.head=n # assigning the n node value reference into the head pointer
    def insert_at_end(self,data):
        n =Node(data)
        if self.start is None:
            self.start=n
        else:
            temp =self.start
            while temp.next is not None:
                temp =temp.next
            temp.next =n
    def search_element(self,data):
        temp =self.start
        while temp is not None:
            if temp.data==data:
                return data
            temp =temp.next
      
        return "element not found"
    
    def insert_at_specified(self,data,position):
        n =Node(data)
        if position==1:
            n.next =self.start
            self.start =n
        else:
            temp =self.start
            for i in range(position-2):
                temp =temp.next
            n.next =temp.next
            temp.next= n
    def print_elements(self):
        temp =self.start
        while temp is not None:
            print(temp.data,end ='--->')
            temp =temp.next
        print(None)
    
    def del_at_beginning(self):
        temp =self.start
        if self.start is not None:
            self.start =temp.next
        else:
            print("the linked list is empty no item to delete")
    def del_at_end(self):
        pre=self.start
        temp =self.start.next
        if self.start is None:
            return
        if self.start.next is None:
            self.start =None
        elif self.start is not None:
            while temp is not None:
                temp =temp.next
                pre =pre.next
            pre.next=None
    def del_at_specified(self,position):
        temp =self.start.next
        pre =self.start
        for i in range(position-1):
            pre =pre.next
            temp = temp.next
        pre.next =temp.next
        temp.next =None
    
    def __iter__(self):
        return Iterable(self.start)



class Iterable:
    def __init__(self,start):
        self.current =start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            StopIteration
        data =self.current.data#just like temp we traverse is similar way using self.current we traverse through each element
        self.current= self.current.data
        return data



          
      
        



    

        
    



    


 