class Node:
    def __init__(self,data =None,next =None):
        self.data =data #n1.next =5
        self.next =next # n1.next =None
class Sll:
    
    def __init__(self,head =None):
        self.head =head #sll.head =none
    
    def is_empty(self):
        return self.head is None
    
    def traverse(self):
        if self.head is None:
            print("linkled list is empty")
        else:
            a =self.head
            while a is not None: # no because by ssl.head =n1
                print(a.data,end ='-->') #n1.data,n2.data,n3.data,
                a=a.next #n1.next =n2
            print(None)
    
    def insert_at_beginning(self,data):
    
        nb =Node(data)
        nb.next =self.head #will create a link between nb and n1 node
        self.head =nb # as head will piont to the first node therefore now head will point to wards nb
    
    def insert_at_end(self,data):
        ne =Node(data)
        a =self.head
        while a.next is not None:
            a =a.next
        a.next =ne
    
    def insert_at_specified(self,data,position):
        nas =Node(data)
        a =self.head
        for i in range(1,position-1):
            a =a.next
        nas.next =a.next
        a.next =nas
    
    def del_at_beginning(self):
        if self.head is None:
            print("no element to delete")
            return
        elif self.head.next is None:
            self.head =None
        else:
            self.head=self.head.next



    
    def del_at_ending(self):
        a=self.head.next
        pre =self.head
        while a.next is not None:
            a =a.next
            pre =pre.next
        pre.next =None
    def del_at_specific(self,position):
        
        a =self.head.next
        pre =self.head
        for i in range(1,position-1):
            a =a.next
            pre =pre.next
        pre.next =a.next
        a.next =None
    
    def search(self,item):
        a =self.head
        while a is not None:
            if item==a.data:
                print(a.data)
            a =a.next
        return None
    


class iterator:
    def __init__(self,start):
        self.current =start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current= self.current.next

        
        







