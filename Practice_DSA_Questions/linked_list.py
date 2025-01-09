# ---------------------------------- linked list in python


# ---creating a node
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

# --- creating a linked list
class LinkedList:
    def __init__(self):
        self.head=None

    # adding node to linked list
    def add_node(self,value):
        new_node=Node(value)

        # creating head node
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node

l1=LinkedList()
l1.add_node(10)
l1.add_node(24)
l1.add_node(54)

# print(l1.head.data)
# print(l1.head.next)

# print(l1.head.next.data)
# print(l1.head.next.next)

# print(l1.head.next.next.data)
# print(l1.head.next.next.next)
# print("\n")


# -------------------------- displaying the linked list
def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next

# print_linked_list(l1.head)

# ------------------------ displaying linked list using recursion
# def print_recursively(head):
#     if head is None:
#         return
#     else:
#         print(head.data)
#         print_recursively(head.next)

# print_recursively(l1.head)


# ---------------------- inserting values by iteratiably
l2=LinkedList()
for i in range(10):
    l2.add_node(i*2)

print_linked_list(l2.head)
print("\n")


# ----------------------- counting the no of nodes created
def find_length(head):
    length=0
    while head is not None:
        length+=1
        head=head.next
    return length

print(find_length(l2.head))


# -----------same finding length recursively
# def find_length_recursively(head):
#     if head is None:
#         return 0
#     else:
#         return 1+ find_length_recursively(head.next)

# print(find_length_recursively(l2.head))