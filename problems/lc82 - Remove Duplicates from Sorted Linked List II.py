# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# TODO: Incomplete
def deleteDuplicates(head: ListNode) -> ListNode:
    # this function is for use on a SORTED linked list and is much faster
    # since the list is sorted, it would look something like [1,2,3,3,4,5,6,6,6,6,7]
    # in this case, we can determine if something is duplicate if we encounter it two times in a row (or more)
    # so compare element i to element i+1, and so on

    # this is different from lc83 – Remove Duplicates from Sorted Linked List in one way
    # if there is a duplicate, remove it entirely, all instances of it
    # eg: [1,2,2,3,4,4,5] --> [1,3,5], 2 and 4 are duplicates

    if not head: return head

    placeholder = ListNode(-1) # temporary placeholder, can't be None otherwise loop doesn't execute when accessing prev node
    prev = placeholder
    prev.next = head
    curr = head

    while curr:
        # lets say we encounter elements like so: [1,2,2,3,4,4,5]
        # ==> outputs [1, 3, 5], we start at 1, check the next node is distinct,
        # then start at 2, the next node however is 2, so we skip ahead in the while loop
        # until the value is different, ie: at node 3,
        # and then assign prev node's (current is 2, prev is 1) to 3
        # so then we have [1,3,4,4,5].. And continue in this fashion
        if curr.next and curr.val != curr.next.val:
            prev = curr
            curr = curr.next
            continue
        else:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            prev.next = curr.next
            curr = curr.next
    return placeholder.next


a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(1)
a.next.next.next = ListNode(2)
a.next.next.next.next = ListNode(3)
a.next.next.next.next.next = ListNode(3)
a.next.next.next.next.next.next = ListNode(3)
a.next.next.next.next.next.next.next = ListNode(3)
a.next.next.next.next.next.next.next.next = ListNode(3)

# curr = a

deleteDuplicates(a)
curr = a
while curr:
    print(curr.val)
    curr = curr.next