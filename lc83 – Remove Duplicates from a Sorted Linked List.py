# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head: ListNode) -> ListNode:
    # goal is to trim duplicates from the list and return the head of the list
    # approach? Iterate through the list, keep track of elements we've encountered and
    # keep track of the previous node and the current node, if we encounter a duplicate, set prev.next = curr.next,
    # this way we cut out the current node (which is a duplicate) from the list

    # Execution time on this is slow! Important to note that this works on sorted and non-sorted linked lists

    if not head:
        return head

    prev = head
    curr = head.next
    elements_encountered = [prev.val]


    while curr:
        if curr.val in elements_encountered:
            # encountered a duplicate element
            prev.next = curr.next # cut out the curr node from the list
            curr = prev.next
        else:
            elements_encountered.append(curr.val)
            prev = curr
            curr = curr.next
    return head


def sortedDeleteDuplicates(head: ListNode) -> ListNode:
    # this function is for use on a SORTED linked list and is much faster
    # since the list is sorted, it would look something like [1,2,3,3,4,5,6,6,6,6,7]
    # in this case, we can determine if something is duplicate if we encounter it two times in a row (or more)
    # so compare element i to element i+1, and so on
    if not head: return head

    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(3)
a.next.next.next.next = ListNode(3)
a.next.next.next.next.next = ListNode(3)
a.next.next.next.next.next.next = ListNode(4)
a.next.next.next.next.next.next.next = ListNode(4)
a.next.next.next.next.next.next.next.next = ListNode(5)

# curr = a

sortedDeleteDuplicates(a)
curr = a
while curr:
    print(curr.val)
    curr = curr.next
