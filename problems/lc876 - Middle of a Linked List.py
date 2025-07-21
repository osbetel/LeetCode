


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_linked_list(head):
    n = ListNode(val=head[0])
    curr = n
    for x in head[1:]:
        curr.next = ListNode(val=x)
        curr = curr.next
    return n

def middleNode(head):
    # single linked list
    # if length of list is odd return the middle
    # if length of list is even return the second middle node
    # -> find length of linked list
    # -> go to middle
    num_nodes = 1
    n = head
    while n.next is not None:
        num_nodes += 1
        n = n.next

    if num_nodes % 2 == 0:
        num_nodes = ((-1*num_nodes) // 2) * -1
    else:
        num_nodes = num_nodes // 2

    n = head
    for i in range(num_nodes):
        n = n.next
    return n

head = [1,2,3,4,5]
n = construct_linked_list(head)
print(middleNode(n))
