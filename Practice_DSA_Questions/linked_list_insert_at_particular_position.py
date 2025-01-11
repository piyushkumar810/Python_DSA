# ---------- inserting at the particular position of the linked list

class Node():
    def __init__(self, value):
        self.data=value
        self.next=None

def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

# print_linked_list(head)

# now inserting the Node at any position

def insert_at_position(head, value, position):
    new_node=Node(value)

    if position == 1:
        new_node.next=head
        return new_node
    
    current=head
    for i in range(1, position-1):
        if current is None:
            print("invalid position")
            return head
        current=current.next
    
    if current is None:
        print("invalid position")
        return head
    
    new_node.next=current.next
    current.next=new_node

    return head

head=insert_at_position(head, 60, 2)
# head=insert_at_position(head, 50, 1)
# head=insert_at_position(head, 90, 7)
# head=insert_at_position(head, 250, 6)

# print_linked_list(head)