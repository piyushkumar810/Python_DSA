# -------------------------- level order traversal ---------------------------

# from collections import deque

# def level_order(root):
#     if root is None:
#         return
#     else:
#         queue= deque([root])

#         while queue:
#             node=queue.popleft()
#             print(node.val, end=" ")
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)


# -------------------- without using collection module
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

def level_order(root):
    if root is None:
        return
    else:
        queue = [root]  # Using a list instead of deque

        while queue:
            node = queue.pop(0)  # Popping the first element (FIFO behavior)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

level_order(root)