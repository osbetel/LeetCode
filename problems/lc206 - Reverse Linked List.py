"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val,
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    # approach - three pointers I think, one for the current, one for the previous, and one for the next. O(n) time
    # 1) save current.next => temp
    # 2) set current.next = prev
    # 3) set prev = current
    # 4) go to next and repeat
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def printList(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next


def constructList(array):
    if not array:
        return None
    
    head = ListNode(array[0])
    current = head
    
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next
    
    return head
    

arr = [1,2,3,4,5]
l1 = constructList(arr)
# printList(l1)
l2 = reverseList(l1)
printList(l2)