# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    return true if trees p and q are equivalent
    false otherwise. I think that in this case a dfs would be ideal
    and if there is a mismatch at any point then it is invalidated
    O(min(m, n)) complexity where trees have m, n leaves
    """
    def dfs(p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return dfs(p.left, q.left) and dfs(p.right, q.right)

    return dfs(p, q)



a = constructTree([3,9,20,None,None,15,7])
b = constructTree([3,9,20,None,None,15,7])
print(isSameTree(a, b))

