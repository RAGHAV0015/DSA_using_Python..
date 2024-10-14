class Node:
    def __init__(self,right=None,left=None,data=None):
        self.right=right
        self.left=left
        self.data=data

class Binary_tree:
    def __init__(self,root=None):
        self.root=root
    
    def traverse_in_order(self,root):
        if root is None:
            return None
        if root is not None:
            self.traverse_in_order(root.left)
            print(root.data,end=' ')
            self.traverse_in_order(root.right)
    
    def count(self,root):
        if root is not None:
            x=self.count(root.left)
            y=self.count(root.right)
            return x+y+1
        else:
            return 0
    
    def height(self,root):
        if root is not None:
            x=self.height(root.left)
            y=self.height(root.right)
            return max(x,y)+1
    # insert using recurssion  
    def insert(self,root,data):
        n=Node(data=data)
        if root is not None:
            if root.data>data:
                root.left=self.insert(root.left,data)
            elif root.data<data:
                root.right=self.insert(root.right,data)
            
            return root #returning the reference of the root
        else:
            return n
    #insert using loop
    def insert_using_loop(self,data,root):
        n=Node(data)
        if root is None:
            return n
        else:
            parent=None
            current=root
            while current is not None:
                parent=current
                if current.data>data:
                    current=current.left
                elif current.data<data:
                    current=current.right
            if parent.data>data:
                parent.left=n
            else:
                parent.right=n
        return root #returning the reference of the root
    
    def min_element(self,root):
        if root is None:
            print("no element to find min ")
            return None
        else:
            current=root
            while current is not None:
                current=current.left
            return current
        

    
    def del_node(self,data,root):
        if root is None:
            print(f"the element {data} not found")
            return None

        if root is not None: #condition checking wether the root is none or not
            if root.data>data:
                root.left=self.del_node(data,root.left)
            elif root.data<data:
                root.right=self.del_node(data,root.right)
            else:# found the target node to delete
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                temp=self.min_element(root.right)
                root.data=temp.data
                root.right=self.del_node(temp.data,root.right)
        return root   
    
    def search(self,data,root):
        if root is None:
            return None
        elif root.data==data:
            return f"found the data---> {data}"
        else:
            if root.data>data:
                return self.search(data,root.left)
            else:

                return self.search(data,root.right)

                
n1=Node(data=1)
n2=Node(data=2)
n3=Node(data=3)
n4=Node(data=4)
n5=Node(data=5)
n6=Node(data=6)
n7=Node(data=7)

bt=Binary_tree()
bt.root=n4
n4.left=n2
n4.right=n6
n2.left=n1
n2.right=n3
n6.left=n5
n6.right=n7


bt.traverse_in_order(bt.root)
bt.del_node(5,n4)
print()
bt.traverse_in_order(bt.root)
print()
bt.insert(n4,66)
bt.traverse_in_order(bt.root)
print()
print(bt.height(n4))
print()
print(bt.count())
print()
print(bt.min())

print(bt.search(data=6,root=n4))