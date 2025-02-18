# ------------------------- implementation of stack with linked list --------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("stack is empty")  # Changed ImportError to IndexError
        popped_value = self.head.data
        self.head = self.head.next
        return popped_value

    def print(self):
        temp = self.head  # Use a temp variable to traverse
        while temp is not None:
            print(temp.data)
            temp = temp.next  # Move temp instead of self.head

# if __name__=="__main__":
s = Stack()
s.push(7)
s.push(4)
s.push(28)
s.print()  # Output: 28 4 7
print("---")
s.pop()
s.print()  # Output: 4 7
