

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.name = None

def getIntersectionNode(headA: ListNode, headB: ListNode):
    if headA is None or headB is None: return None

    a = headA
    b = headB

    count = {}

    while a is not None:
        addOne(count, a)
        # print(a.val)
        a = a.next
    while b is not None:
        if count.__contains__(b):
            return b
        b = b.next
    return None
    # print(count)

    if len(count) == 0: return None
    r = max(count, key=count.get)
    if count.get(r) == 1: return None
    else: return r


def addOne(dic: dict, key):
    if dic.get(key) is None:
        dic.update({key: 1})
    else:
        dic.update({key: dic.get(key) + 1})


def makeList(i: [int], name):
    r = ListNode(i[0])
    r.name = (name + str(0))
    n = r
    for k in range(1, len(i)):
        n.next = ListNode(i[k])
        n.name = (name + str(k))
        n = n.next
    return r


# r = makeList([1,3,5,7,9,11,13,15,17,19,21], "r")
# s = makeList([2], "s")
# print(getIntersectionNode(r,s) is None) # True
#
# r = makeList([1,2,3,4,5,6,7,8,9,10,11,12,13], "r")
# s = makeList([1,2,3,4,5,6,7,8,9,10,11,12,13], "s")
# print(getIntersectionNode(r,s) == r) # True, intersect starting at 1
#
# r = makeList([1,2,3,4,5,6], "r")
# s = makeList([6,7,8], "s")
# print(getIntersectionNode(r,s).val == 6) # True

a1 = ListNode(1)
a2 = ListNode(2)
a1.next = a2








