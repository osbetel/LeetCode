
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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # approaches:
    # 1) we can write a function to read linked lists into integers, add the integers, and have a function to turn
    #       integers back into linked lists, reversed and all. Downside is that it would be O(n + k + j), where
    #       n, k, j are the lengths of the two input lists, and expected output list.
    # 2) Note that the lists are in reverse order though, which means the place / base of the numbers
    #       goes ones -> tens -> hundreds... so on. This means that adding one to another directly is fine
    #       because, should we need to "carry a one," then it simply gets tacked onto the next node.
    #       This of course overwrites one of the lists as we do it in-place instead of creating a new list.

    result = ListNode(0)
    result_tail = result
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        carry, out = divmod(val1 + val2 + carry, 10)

        result_tail.next = ListNode(out)
        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next

def printListNode(l: ListNode):
    c = l
    while c is not None:
        print(c.val)
        c = c.next


a = ListNode(8)
b = ListNode(9)
c = ListNode(9)
# a = ListNode(1)
a.next = b
b.next = c

# i = ListNode(5)
# j = ListNode(6)
# k = ListNode(4)
i = ListNode(2)
# j = ListNode(9)
# i.next = j
# j.next = k


num = addTwoNumbers(a, i)
printListNode(num)
# printListNode(a)
# print()
# printListNode(i)







