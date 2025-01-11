# ---------------------- deletion at particular value

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

# ---------------------------  deletion of a particular value
def deleting_particular_value(head, value):
    # if no element in linked list
    if head is None:
        print("no element in linked list")
        return None
    
    # if 1st element is the value which we want to delete
    if head.data==value:
        new_head=head.next
        head.next=None
        return new_head
    
    # if any value(means the value which is given to delet) we want to delete form no of linked list
    current=head
    while current.next is not None and current.next.data != value:
        current=current.next
    if current.next is None:
        print("value not found")
        return head
    
    temp=current.next
    current.next=current.next.next
    temp.next=None
    return head

head=deleting_particular_value(head,50)
# head=deleting_particular_value(head,20)
# head=deleting_particular_value(head,0)

print_linked_list(head)