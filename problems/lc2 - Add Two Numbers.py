from typing import Optional
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
    # give two non empty linked lists where the digits as stored in reverse order,
    # each node contains a single digit
    # this means first node is ones place, second is tens, then hundreds, etc
    # 1) put a pointer at the start of each list, 
    # 2) iterate and add one at a time, accounting for carrying 10+
    # 3) when one of the pointers has self.next is None, set to 0 and continue iteration until we run out
    assert l1 is not None and l2 is not None

    # pointers
    p1: ListNode = l1
    p2: ListNode = l2
    root = ListNode(0, None)
    r = root
    carry = 0

    while p1 is not None or p2 is not None or carry:
        # get values from current nodes
        val1 = p1.val if p1 else 0
        val2 = p2.val if p2 else 0
        
        # add current nodes plus carry
        v = val1 + val2 + carry
        carry = v // 10
        v = v % 10
        
        # create new node with the digit
        r.next = ListNode(v, None)
        r = r.next

        # move pointers forward if they exist
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None

    return root.next
        

def printListNode(l: ListNode):
    r = []
    c = l
    while c is not None:
        r.append(c.val)
        c = c.next
    print(r)
    return r


def construct_list(l: [int]):
    root = ListNode(0, None)
    r = root
    for i in range(len(l)):
        r.val = l[i]

        # avoid trailing 0 node
        if i < len(l) - 1:
            r.next = ListNode(0, None)
            r = r.next

    return root

a = [
    [2, 4, 3],
    [9,9,9,9,9,9,9],
    [0],
    [9, 9]
]
b = [
    [5, 6, 4],
    [9,9,9,9],
    [0],
    [9, 9]
]

for i, j in zip(a, b):
    k = addTwoNumbers(construct_list(i), construct_list(j))
    printListNode(k)









