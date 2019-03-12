# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)
        
        
    def helper(self, node, depth):
        if not node:
            return depth
        else:
            return max(self.helper(node.left, depth+1), self.helper(node.right, depth+1))
        