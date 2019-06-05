"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        self.maxSum = float('-inf')
        self.resNode = None
        self.helper(root)
        return self.resNode
        
    def helper(self, node):
        if not node:
            return 0
        subTreeSum = node.val + self.helper(node.left) + self.helper(node.right)
        
        if subTreeSum > self.maxSum:
            self.resNode = node
            self.maxSum = subTreeSum
        return subTreeSum
