# ----------------- inserting node at the last of the linked list

class Node():
    def __init__(self,value):
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

# inserting a new node in start
def insert_at_start(head,value):
    new_node=Node(value)

    new_node.next=head
    return new_node

head=insert_at_start(head,50)
# head=insert_at_start(head,60)


#  inserting a new node at the end 
def insert_at_end(head,value):
    new_node=Node(value)

    # if the linked list is empty the new node is the only element in the linked list
    if head is None:
        return new_node
    
    else:
        current=head
        while current.next is not None:
            current=current.next
        current.next=new_node

        return head


insert_at_end(head,100)

print_linked_list(head)