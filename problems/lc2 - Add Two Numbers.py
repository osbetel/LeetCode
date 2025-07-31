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
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
    # given two linked lists where the numbers are stored in reverse order, add the numbers and return the sum as a linked list
    # approach - two pointers, one at the end of each list
    # iterate over lists
    # then add numbers into a new list
    # make sure to account for carrying 1 when values add up to 10 or more
    # this of O(m + n) complexity
    left, right = l1, l2
    resultHead = ListNode()
    result = resultHead
    carry = 0

    while left is not None or right is not None:
        lval = left.val if left else 0
        rval = right.val if right else 0
        val = lval + rval + carry

        result.val = val % 10
        carry = val // 10
        
        left = left.next if left else None
        right = right.next if right else None
        
        if left is not None or right is not None or carry > 0:
            result.next = ListNode()
            result = result.next

    if carry > 0:
        result.val = carry

    return resultHead
    



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
    # [9,9,9,9,9,9,9],
    # [0],
    # [9, 9]
]
b = [
    [5, 6, 4],
    # [9,9,9,9],
    # [0],
    # [9, 9]
]

for i, j in zip(a, b):
    k = addTwoNumbers(construct_list(i), construct_list(j))
    printListNode(k)









