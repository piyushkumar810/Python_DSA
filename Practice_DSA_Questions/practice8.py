# -------------------------- removing duplicate from sorted list

class Node():
    def __init__(self,value):
        self.data=value
        self.next=None

head=None
head=Node(10)
head.next=Node(12)
head.next.next=Node(12)
head.next.next.next=Node(20)
head.next.next.next.next=Node(28)
head.next.next.next.next.next=Node(28)


def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next

print_linked_list(head)
print("\n")

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

remove_duplicate_element(head)
print_linked_list(head)