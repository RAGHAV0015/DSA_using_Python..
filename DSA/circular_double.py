from typing import Any


class Node:
    def __init__(self,data=None,pre=None,next=None):
        self.next =next
        self.data =data
        self.pre =pre
class Doubly_circular:
    def __init__(self,last=None):
        self.last =last
    
    def insert_at_beginning(self,data):
        n=Node(data)
        if self.last is None:
            self.last=n
            self.last.pre =n
            self.last.next =n
        else:
            n.next =self.last.next
            self.last.next.pre =n
            self.last.next =n
            n.pre=self.last
    
    def insert_at_last(self,data):
        n =Node(data)
        
        if self.last is None:
            self.last =n
            n.pre =self.last
            self.last.pre =n
            self.last.next =n
        else:
            n.next=self.last.next
            self.last.next.pre =n
            self.last.next =n
            n.pre =self.last
            self.last =n
        
    def traverse_from_beginning(self):
        if self.last is None:
           print("traverse is not possible")
        else:
            temp =self.last.next
            while True:
                if temp is not None:
                    print(temp.data,end =' ')
                    temp =temp.next
                    if temp==self.last.next:
                        break
    
    def traverse_from_end(self):
        if self.last is None:
            print("cant traverse the list")
        else:
            temp=self.last
            while True:
                print(temp.data,end =' ')
                temp =temp.pre
                if temp==self.last:
                    break

    def del_at_first(self):
        if self.last is None:
            print("no element to delete")
        elif self.last.next==self.last:
            self.last =None
        else:
            self.last.next=self.last.next.next

    def del_at_end(self):
        if self.last is None:
            print("no element to del")
        elif self.last.next==self.last:
            self.last=None
        else:
            temp =self.last.next
            while temp.next!= self.last:
                temp =temp.next   
            temp.next=self.last.next
            self.last=temp
    
    def insert_at_specific(self,data,position):
        n =Node(data)
        if position==1:
            if self.last is None:
                self.last =n
                n.next =self.last
                n.pre =self.last
            else:
                n.next=self.last.next 
                self.last.next =n
                self.last.next.pre=n
                n.pre =self.last
        else:
            temp =self.last.next
            for i in range(position-2):
                temp=temp.next
                if temp==self.last.next:
                    print("out of range position")
                    return
            n.next =temp.next
            temp.next =n
            n.pre=temp
            
    def del_at_specific(self,postion):
        if self.last is None:
            print("nothing to delete")
            return
        if postion==1:
            if self.last.next ==self.last:
                self.last =None
            else:
                self.last.next=self.last.next.next
                self.last.next.pre =self.last
        else:
            temp =self.last.next
            for i in range(postion-2):
                temp =temp.next
                if temp==self.last:
                    print("the deletion is out of range ")
                    return
            temp.next =temp.next.next
            temp.next.next.pre =temp
    
    def __iter__(self):
        return iterator(self.last)               




class iterator:
    def __init__(self,last):
        self.current =last
        self.last=last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if  self.current == self.last.next:
            raise StopIteration
        data =self.current.data
        self.current=self.current.next
        return data
            

    
    




n1=Node(data=1)
n2 =Node(data=2)
n3 =Node(data=3)
n4 =Node(data=4)
cdl =Doubly_circular()
cdl.last =n4
n1.next=n2
n2.next =n3
n3.next=n4
n1.pre =n4
n2.pre =n1
n3.pre =n2
n4.pre =n3
n4.next =n1
cdl.traverse_from_beginning()
print()
cdl.traverse_from_end()
cdl.del_at_first()
print()
cdl.insert_at_specific(6,3)
cdl.del_at_specific(7)

cdl.traverse_from_beginning()
for x in cdl:
    print(x,end=" ")
