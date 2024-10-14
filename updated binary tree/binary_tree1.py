
class Node:
    
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.right =right
        self.left =left
    
class Binary_Search_Tree:
    
    def __init__(self,root=None):
        self.root =root
    
   
    # this is pre ordered traverse +ab
    
    def traverse(self,Node):
        if Node is not None:
            print(Node.data,end=' ')
            self.traverse(Node.left)
            self.traverse(Node.right)
    
    # this is FOR inorder
    
    def traverse_inorder(self,node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data,end=' ')
            self.traverse_inorder(node.right)    
    
    # this is for traversel post order ab+
   
    def traverse_post(self,Node):
        if Node is not None:
            self.traverse_post(Node.left)
            self.traverse_post(Node.right)
            print(Node.data,end=' ')
            
    
   
   
   
    def count(self, node):
    # Base case: if the node is None, return 0 (no nodes to count)
        if node is None:
            return 0
    
    # Recursive case: count nodes in left and right subtrees
        left_count = self.count(node.left)
        right_count = self.count(node.right)
    
    # Return total count (1 for the current node + left_count + right_count)
        return left_count + right_count + 1

    def height_of_tree(self,node):
        if node is  None:
            return 0
        x=self.height_of_tree(node.left)
        y=self.height_of_tree(node.right)
        return max(x,y) + 1
    

    def delete_element(self,data,node):
        if node is None:
            print("no data to delete")
            return
        if node.data>data:
            node.left=self.delete_element(data,node.left)
        elif node.data<data:
            node.right=self.delete_element(data,node.right)
        else:
            if node.left is None and node.right is None:
                node=None
                return node
            elif node.left is None:
                temp=node.right
                node=None
                return temp
            elif node.right is None:
                temp=node.left
                node=None
                return temp
            temp=self.min_val(node.right)
            node.data=temp.data
            node.right=self.delete_element(temp.data,node.right)
        return node
             

        
                
    

























































# Creating the nodes for the tree
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Manually linking the nodes to form a binary search tree
#       3
#      / \
#     1   4
#      \
#       2
#          \
#           5
root = node3           # Root node is 3
root.left = node1      # Left child of 3 is 1
root.right = node4     # Right child of 3 is 4
node1.right = node2    # Right child of 1 is 2
node2.right = node5  
# Create binary search tree
bst = Binary_Search_Tree(root)

# Creating the Binary Search Tree and assigning the root
print()
# Pre-order traversal
print("Pre-order Traversal:")
bst.traverse(bst.root)  # Output: 3 1 2 4 5
print()
# In-order traversal
print("\nIn-order Traversal:")
bst.traverse_inorder(bst.root)  # Output: 1 2 3 4 5
print()
# Post-order traversal
print("\nPost-order Traversal:")
bst.traverse_post(bst.root)  # Output: 2 1 5 4 3

print()
# Count the total number of nodes
total_nodes = bst.count(bst.root)
print("Total nodes:", total_nodes)

height=bst.height_of_tree(root)
print(height)