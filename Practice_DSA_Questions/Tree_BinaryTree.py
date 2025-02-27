# ----------------------------------- Binary Tree implementation ------------------------------

class Node:
    def __init__(self,value):
        self.left=None
        self.val=value
        self.right=None
    
    # def display(self,root):
    #     if root is None:
    #         return None
    #     else:
    #         print(root.val)
    #         self.display(root.left)
    #         self.display(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.left.left.left=Node(8)


# displaying all data of the tree
def display(root):
    if root is None:
        return None
    else:
        print(root.val)
        display(root.left)
        display(root.right)

display(root)
print()


# sum of nodes of the binary tree
def sum_of_node(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return root.val
    else:
        return root.val+sum_of_node(root.left)+sum_of_node(root.right)
    
result=sum_of_node(root)
print(f"the sum of nodes of binary tree is = {result}")
print()


# finding the max of the tree
def max_of_tree(root):
    if root is None:  
        return None  # If the tree is empty, return None
    
    # Recursively find the maximum in left and right subtrees
    left_max = max_of_tree(root.left)
    right_max = max_of_tree(root.right)
    
    # Find the largest value among root, left_max, and right_max
    max_node = root  # Start by assuming the root has the largest value
    
    if left_max and left_max.val > max_node.val:
        max_node = left_max  # Update if left child is greater
    
    if right_max and right_max.val > max_node.val:
        max_node = right_max  # Update if right child is greater

    return max_node  # Return the node with the maximum value

# Example usage (assuming 'root' is defined)
maximum = max_of_tree(root)

if maximum:
    print(f"Maximum value in the tree: {maximum.val}")
else:
    print("The tree is empty.")
print()


# height of the binary tree
def height_of_tree(root):
    if root is None:
        return -1
    else:
        left_height=height_of_tree(root.left)
        right_height=height_of_tree(root.right)

        return 1+max(left_height,right_height)
    
tree_height=height_of_tree(root)
print(f"height of tree = {tree_height}")