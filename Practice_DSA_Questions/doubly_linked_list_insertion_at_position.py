# ------------------------- doubly linked list insertion a value at position

class Node:
    def __init__(self,value):
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

    def insertion_at_position(self,value,position):
        new_node=Node(value)

        if position==0:
            self.insertion_at_start(value)

        else:
            current=self.head
            for i in range(1,position-1):
                current=current.next

                if current is None:
                    raise IndexError("position out of box")
            
            new_node.next=current.next
            new_node.prev=current

            if current.next:
                current.next.prev=new_node
            current.next=new_node



def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next


dl=doubly_linked_list()
dl.insertion_at_start(10)
dl.insertion_at_end(20)
dl.insertion_at_position(40,2)
print_linked_list(dl.head)