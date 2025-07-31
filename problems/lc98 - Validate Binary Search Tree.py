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
def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    given the root of a bst determine if the tree is valid. return true if it is, false if not
    bst is valid if all the left nodes are strictly less than the parent and right nodes are greater than the parent
    approach - O(n) time, use a DFS, check values, and then return false if invalid. base case return true
    """
    def dfs(node: TreeNode, min_bound=float("-inf"), max_bound=float("inf")):
        if not node:
            return True

        if node.val <= min_bound or node.val >= max_bound:
            return False
    
        return dfs(node.left, min_bound, node.val) and dfs(node.right, node.val, max_bound)
    
    return dfs(root)


tests = [
    [2,1,3],
    [3,9,20,None,None,15,7],
    [5,1,4,None,None,3,6]
]
for t in tests:
    a = constructTree(t)
    print(isValidBST(a))