# ----------------------------- doubly linked list insertion at end

class Node:
    def __init__(self, value):
        self.prev=None
        self.data=value
        self.next=None

class doubly_linked_list:
    def __init__(self):
        self.head=None

    def insertion_at_start(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node

        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def insertion_at_end(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node

        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
            new_node.prev=current



def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next


dl=doubly_linked_list()
dl.insertion_at_start(10)
dl.insertion_at_end(20)
print_linked_list(dl.head)