# Merge k sorted linked lists and return it as one
# sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists: [ListNode]) -> ListNode:
    """
    So we're given a list of nodes, each node being the head of a singly-linked list
    Approach: Suppose we are given
        1->4->5,
        1->3->4,
        2->6
        The head nodes are currently 1, 1, and 2.
        What if we construct the new singly linked list by selecting the minimum node each time?
        (if two nodes are equal, like the first 1 and second 1, it doesn't matter)
        This means we need to be able to find the minimum value of all the head nodes at all times
        and we need to be able to do this efficiently as well...
    """

    if not lists: return None

    temphead = ListNode(-1)
    prev = temphead
    minNode = None
    idxToPop = -1
    while lists:
        # this for loop finds the minimum head node in the current list
        # meaning that it's O(k), where k is the number of lists
        for i in range(len(lists)):
            if not lists[i]: continue
            if not minNode: minNode = lists[i]
            if lists[i].val <= minNode.val:
                minNode = lists[i]
                idxToPop = i

        # additionally, since we must go through every element of the k lists, we have O(kn),
        # where n is num of total elements.
        # overall time complexity of O(kn), space complexity is O(1)

        prev.next = minNode
        prev = minNode
        minNode = None

        if idxToPop == -1: return None # this should have changed

        if not lists[idxToPop].next:
            lists.remove(lists[idxToPop])
        else:
            lists[idxToPop] = lists[idxToPop].next

    return temphead.next


def nlogkMergeKLists(lists: [ListNode]) -> ListNode:
    """
    We can also approach this similar to merge sort! Pair up lists into 2's when possible and merge them into
    a larger sorted linked list. Repeat this process until we have a final list.
    """

    if not lists: return None

    while len(lists) > 1:
        for i in range(len(lists) // 2):
            left = lists.pop(i)
            if len(lists) > 1:
                right = lists.pop(i + 1)
            else:
                right = lists.pop(i)
            lists.append(mergePair(left, right))
            # IMPORTANT: newly appended items go to the end of the list!
            # ie: they won't be accessed during this for loop
    return lists[0]


def mergePair(head1, head2):
    temphead = ListNode(-1)
    curr = temphead
    while head1 and head2:
        if head1.val <= head2.val:
            curr.next = head1
            curr = head1
            head1 = head1.next
        else:
            curr.next = head2
            curr = head2
            head2 = head2.next

    while head1:
        curr.next = head1
        curr = head1
        head1 = head1.next

    while head2:
        curr.next = head2
        curr = head2
        head2 = head2.next

    return temphead.next

a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
c = ListNode(2)
c.next = ListNode(6)
heads = [a,b,c]
k = mergeKLists(heads)

while k:
    print(k.val)
    k = k.next





