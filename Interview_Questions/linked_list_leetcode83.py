# -------------------------- removing duplicate from sorted list

class Node():
    def __init__(self,value):
        self.data=value
        self.next=None

class linked_list():
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

l1=linked_list()
list=[10,20,20,30,35,35,40,40]
n=len(list)
for i in range(n):
    l1.add_node(list[i])


def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next

print_linked_list(l1.head)

def remove_duplicate_element(head):
    if head is None or head.next is None:
        return head
    
    else:
        slow=head
        fast=head.next

        # while fast is not None:
        while fast:
            if slow.data== fast.data:
                slow.next=fast.next
            else:
                slow=slow.next
            fast=fast.next
        
        return head
    
print("\n")
remove_duplicate_element(l1.head)
print_linked_list(l1.head)


# --------------what is the difference between both condition
# while fast is not None:
# while fast:
''' For linked list traversal, both forms are functionally equivalent. The choice between the two often comes down to style preference:
        while fast:-- is common and concise.
        while fast is not None:-- is more explicit and can make the condition easier to understand, especially for beginners.'''