# # ---------------------- deletion of node at end of the linked list

class Node():
    def __init__(self, value):
        self.data=value
        self.next=None

def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next

head=None
head=Node(20)
head.next=Node(30)
head.next.next=Node(40)
head.next.next.next=Node(50)

# print_linked_list(head)
#----------------- deletion of node at end
def deletion_at_end(head):
    # if no elements are in the linked list
    if head is None:
        print("there is no node to delete")
        return None
    
    # if only one element are there in the linked list
    elif head.next is None:
        return None
    
    # if no of elements are there in linked list
    else:
        current=head
        while current.next.next is not None:
            current=current.next
        current.next=None
        return head
        

head=deletion_at_end(head)
print_linked_list(head)