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
def maxDepth(root: Optional[TreeNode]) -> int:
    # given the root of a binary tree, find the max depth
    # approach - does a BFS vs DFS really matter? I suppose I would go DFS as that searches down the tree
    # BFS is also a little more tedious to implement as it needs a queue or deque
    # DFS O(n) time as we need to search every node and path
    if not root:
        return 0
    
    heights = set()
    def dfs(node: TreeNode, height=1): # 1 because the root counts as a level
        # base case, we are at the bottom and node has no more leaves
        if node is None:
            return
        if not node.left and not node.right:
            heights.add(height)
        else:
            # dfs explores all left paths, then all right paths recursively
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)
    
    dfs(root)
    return max(heights)


root = constructTree([3,9,20,None,None,15,7])
print(maxDepth(root))
