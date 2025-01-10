# --------------------- insert a new node at starting of a linked list

class Node():
    def __init__(self, value):
        self.data=value
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def add_node(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node

        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
            
l1=LinkedList()
arr=[5,10,15]
n=len(arr)
for i in range(n):
    l1.add_node(arr[i])

# print(l1.head.data)
# print(l1.head.next.data)
# print(l1.head.next.next.data)


# -----display the linked list
def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next


# ---------------------- inserting a node at the beginning
def insert_at_start(head,value):
    new_node=Node(value)
    
    new_node.next=head
    return new_node

head = insert_at_start(l1.head, 30)
print_linked_list(head)