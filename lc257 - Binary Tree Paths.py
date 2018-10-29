# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.
# Example:
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binaryTreePaths(root: TreeNode, currString, results):

    if root is None:
        results.append(currString[:-2])
        return

    else:
        if root.left is not None:
            binaryTreePaths(root.left, currString + str(root.val) + "->", results)
        if root.right is not None:
            binaryTreePaths(root.right, currString + str(root.val) + "->", results)
        elif root.left is None and root.right is None:
            binaryTreePaths(None, currString + str(root.val) + "->", results)

    return results


r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.right = TreeNode(5)

print(binaryTreePaths(r, "", []))
