class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val

def constructTree(array):
    if not array or array[0] is None:
        return None
    
    root = TreeNode(array[0])
    queue = [root]
    i = 1
    
    while queue and i < len(array):
        node = queue.pop(0)
        
        # Left child
        if i < len(array) and array[i] is not None:
            node.left = TreeNode(array[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(array) and array[i] is not None:
            node.right = TreeNode(array[i])
            queue.append(node.right)
        i += 1
    
    return root

from typing import Optional
from collections import deque
def levelOrder(root: Optional[TreeNode]):
    """
    Given the root of a binary tree, return the level order traversal of it's nodes, from left to right
    this requires a BFS type traversal I think
    """
    # base case
    if not root:
        return []
    
    # at each level, get all the child nodes and then visit them all, using a set if needed to avoid cycles (usually in a graph though)
    # add all children to the queue. start with the root in the queue
    # then for each level put each child in the queue
    # then we process all the nodes of that level
    # O(n) time as we need to hit all nodes on all levels
    queue = deque([root])
    res = []

    while queue:
        level = []

        for _ in range(len(queue)): # we added n nodes from the current level on the previous iteration, process exactly that many
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left) # nodes are added left child first, so order is left to right guaranteed
            if node.right:
                queue.append(node.right)

        res.append(level)

    return res


a = constructTree([3,9,20,None,None,15,7])
print(levelOrder(a))