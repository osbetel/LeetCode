

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

def removeNthFromEnd(head, n):
    if n == 1 and head.next is None:
        return None
    prev = head
    remove_n_ptr = head
    front_ptr = head
    for i in range(n - 1):
        front_ptr = front_ptr.next
    print(remove_n_ptr.val, front_ptr.val)

    while front_ptr.next:
        prev = remove_n_ptr
        remove_n_ptr = remove_n_ptr.next
        front_ptr = front_ptr.next
    print(prev.val, remove_n_ptr.val, front_ptr.val)

    prev.next = remove_n_ptr.next
    return head


head = [1,2]
root = construct_linked_list(head)
root = removeNthFromEnd(root, 2)
while root.next:
    print(root.val)
    root = root.next
print(root.val)
