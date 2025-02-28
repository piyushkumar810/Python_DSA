# -------------------------------------- Tree depth first search --------------------------------

# in_order traversal
# pre_order traversal
# post_order traversal

class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

def display(root):
    if root is None:
        return
    else:
        print(root.val)
        display(root.left)
        display(root.right)

# display(root)
print()

# pre order traversal of tree (root -> left -> right)
def pre_order(root):
    if root is None:
        return
    else:
        print(root.val , end=" ")
        pre_order(root.left)
        pre_order(root.right)

pre_order(root)
print()

# in order traversal of tree (left -> root ->  right)
def in_order(root):
    if root is None:
        return
    else:
        in_order(root.left)
        print(root.val , end=" ")
        in_order(root.right)

in_order(root)
print()

# post order traversal of tree (left -> right -> root)
def post_order(root):
    if root is None:
        return
    else:
        post_order(root.left)
        post_order(root.right)
        print(root.val , end=" ")

post_order(root)