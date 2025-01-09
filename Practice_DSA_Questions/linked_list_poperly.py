# ---------------------------- creating a linked list

class Node():
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
    
    def add_node(self,value):
        # creating a node
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node

l1=LinkedList()

# adding values to LL
arr=[12,42,45,76,45,75,86,35]
n=len(arr)
for i in range(n):
    l1.add_node(arr[i])

# -------------------printing one by one 
print(l1.head.data)
print(l1.head.next)

print("\n")

print(l1.head.next.next.next.next.next.data)


# -------------------displaying the values by using loop
# def print_linked_list(head):
#     while head is not None:
#         print(head.data)
#         head=head.next

# print_linked_list(l1.head)
