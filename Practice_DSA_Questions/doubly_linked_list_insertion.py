# ------------------------------- insertion of node in doubly linked list

class Node:
    def __init__(self, value):
        self.prev=None
        self.data=value
        self.next=None

class doubly_linked_list:
    def __init__(self):
        self.head=None

    def insert_at_start(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node

        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node


def print_linked_list(head):
    current = head
    while current is not None:  # Iterate until `current` is None
        # print(current.prev)    # Print previous address
        '''
        None
        <__main__.Node object at 0x000001EBE54A2B50>
        <__main__.Node object at 0x000001EBE54A2B10>
        '''

        print(current.data)      #print the data 
        '''
        30
        20
        10
        '''

        # print(current.next)
        '''
        <__main__.Node object at 0x0000027318612AD0>
        <__main__.Node object at 0x0000027318612A90>
        None
        '''
        current = current.next

# Example usage
dl = doubly_linked_list()
dl.insert_at_start(10)
dl.insert_at_start(20)
dl.insert_at_start(30)

print_linked_list(dl.head)