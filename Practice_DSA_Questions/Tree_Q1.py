# ---------------------------- Q1. print elements on n th level ----------------------------------------------

class Node:
    def __init__(self, value):
        self.left = None
        self.val = value
        self.right = None

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")
root.left.left.left = Node("H")
root.left.left.right = Node("I")

def print_elements_level_wise(root):
    if root is None:
        return
    elif root.left is None and root.right is None:
        print(f"There is only one level in the tree (Level 0): {root.val}")
        return
    else:
        queue = [root]
        level = 0

        while queue:
            size = len(queue)  # Number of nodes at the current level
            print(f"Level {level}:", end=" ")

            for i in range(size):  
                node = queue.pop(0)
                print(node.val, end=" ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            print()  # Newline after each level
            level += 1

print_elements_level_wise(root)
