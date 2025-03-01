# --------------------------------------- is same tree---------------------------------

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def isSameTree(p, q):
    # If both trees are empty, they are the same
    if not p and not q:
        return True
    # If one tree is empty and the other is not, they are not the same
    if not p or not q:
        return False
    # Check if current node values are the same and recursively check left & right subtrees
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Example Trees
tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)

tree2 = Node(1)
tree2.left = Node(2)
tree2.right = Node(3)

# Check if the two trees are the same
print(isSameTree(tree1, tree2))  # Output: True (both trees are identical)
