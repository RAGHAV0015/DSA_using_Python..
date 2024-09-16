class Node:
    def __init__(self,data =None,next =None):
        self.data =data #n1.next =5
        self.next =next # n1.next =None
class Sll:
    def __init__(self,head =None):
        self.head =head #sll.head
    def traverse(self):
        if self.head is None:
            print("linkled list is empty")
        else:
            a =self.head
            while a is not None: # no because by ssl.head =n1
                print(a.data,end ='-->') #n1.data,n2.data,n3.data,
                a=a.next #n1.next =n2
            print(None)
n1 =Node(5)
n2 =Node(9)
n3 =Node(7)
n4 =Node(1)
sll =Sll() #sll.head = none
sll.head =n1
n1.next =n2
n2.next =n3
n3.next =n4
sll.traverse()


