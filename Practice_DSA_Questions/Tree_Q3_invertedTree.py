# --------------------------------------- inverted binary tree/ mirror tree

class Node:
    def __init__(self, value):
        self.left=None
        self.val=value
        self.right=None

def invertedTree(root):
    if root is None:
        return
    else:
        # swap
        root.left, root.right = root.right, root.left
        invertedTree(root.left)
        invertedTree(root.right)
        return root
    
def display(root):
    if root is None:
        return
    else:
        print(root.val)
        display(root.left)
        display(root.right)

root=Node(4)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(9)

print("Original Tree :")
display(root)
print()

print("inverted Tree :")
invertedTree(root)
display(root)