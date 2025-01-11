# ---------------------- deletion of node at beginning of the linked list

class Node():
    def __init__(self, value):
        self.data=value
        self.next=None

def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next

head=Node(20)
head.next=Node(30)
head.next.next=Node(40)
head.next.next.next=Node(50)

# print_linked_list(head)
#----------------- deletion of node at start
def deletion_at_start(head):
    if head is None:
        print("no element in the linked list")
        return None
    
    else:
        new_head=head.next
        head.next=None
        return new_head


head=deletion_at_start(head)

print_linked_list(head)