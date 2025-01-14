



class Node:
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
list=[10,20,30,40,50]
n=len(list)
for i in range(n):
    l1.add_node(list[i])


def print_linked_list(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next


print_linked_list(l1.head)

def RotateRight(head,k):
    if head is None:
        return head
        
    length=1
    tail=head
    while tail.next:
        tail=tail.next
        length +=1

    k=k%length

    if k==0:
        return head
        
    # find new head
    new_tail=head
    for i in range(length-k-1):
        new_tail=new_tail.next
        
    new_head=new_tail.next
    tail.next=head
    new_tail.next=None

    return new_head
    

print("\n")
head=RotateRight(l1.head, 6)
print_linked_list(head)