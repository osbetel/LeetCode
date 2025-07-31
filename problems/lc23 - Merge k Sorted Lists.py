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


def array_to_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head


def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def mergeKLists(lists: [ListNode]) -> ListNode:
    """
    So we're given a list of nodes, each node being the head of a singly-linked list. merge them all into one linked list
    [
        1->4->5,
        1->3->4,
        2->6
    ]
    =>  1->1->2->3->4->4->5->6
    how do we do this? pointer at the head of each list -> iterate while each pointer is not None -> select minimum pointer
    -> insert into result list. in this case the pointers can be considered as each index of the list of ListNodes
    """
    def merge(a: ListNode, b: ListNode):
        # first lets write something to merge two sorted lists
        # then we can apply divide and conquer -> merge lists in pairs from the bottom up until we have a single merged list
        # how do we merge two linked lists? keep two pointers at the list, add to a new list depending on which value is lower
        # this approach is O(n log k), where n is total number of elements per list, and k is number of lists
        # because we are dividing k lists in half (log_2 k recursion depth)
        # 
        # what about 

        left, right = a, b
        newHead = ListNode(0)
        current = newHead
        while left is not None and right is not None:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        # one of the lists has been exhausted, simply connect the remaining node to the new list
        if left is not None:
            current.next = left
        if right is not None:
            current.next = right

        return newHead.next

    def recursiveMerge(lists):
        # if length of lists greater than 2, divide it in two and recursively merge
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return merge(*lists)
        else:
            return merge(recursiveMerge(lists[:len(lists) // 2]), recursiveMerge(lists[len(lists) // 2:]))

    return recursiveMerge(lists)

arrays = [
    [1,4,5],
    [1,3,4],
    [2,6]
]

heads = [array_to_list(x) for x in arrays]
merged = mergeKLists(heads)
print(list_to_array(merged))


