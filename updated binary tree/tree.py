class Node:
    def __init__(self,right=None,data=None,left=None):
        self.right=right
        self.left=left
        self.data=data

class Bts():
    def __init__(self,root=None):
        self.root=root
    
    def insert(self,root,data):
        n=Node(data=data)
        if root is not None:
            if root.data>data:
                root.left=self.insert(root.left,data)
            elif root.data<data:
                root.right=self.insert(root.right,data)
            return root
        else:
            return n
    
    def search(self,data,root):
        if root is None or root.data==data:
            return root
        else:
            if root.data > data:
                return self.search(data,root.left)
            else:
                return self.search(data,root.right)
    
    def in_order_treaverse(self,root):
        if root is  None:
            print("the tree is empty")
            return
        self.in_order_treaverse(root.left)
        print(root.data,end=' ')
        self.in_order_treaverse(root.right)
    
    def min_element(self,root):
        if root is  None:
            print("the tree is empty")
            return
        
        while root.left is not None:
            root=root.left
        return root.data
        


    def del_element(self,root,data):
        if root is None:
            print("the tree is empty")
            return None
   
        if root.data>data:
            root.left=self.del_element(root.left,data)
        elif root.data<data:
            root.right=self.del_element(root.right,data)
        # case when the node has one child or no child
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
                # case when the node has 2 child
            temp=self.min_element(root.right)
            root.data=temp.data
            root.right=self.del_element(root.right,temp.data)
       
        return root

    

        
        




