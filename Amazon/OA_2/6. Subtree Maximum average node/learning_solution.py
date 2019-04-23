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
    @return: the root of the maximum average of subtree
    """
    targetNode, targetAverage = None, 0
    
    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.targetNode
        
    def helper(self, node):
        # return (sum, size)
        if not node:
            return (0, 0)
        
        # divide
        left_sum, left_size = self.helper(node.left)
        right_sum, right_size = self.helper(node.right)
        
        # conquer
        sum = left_sum + right_sum + node.val
        size = left_size + right_size + 1
        if not self.targetNode or self.targetAverage < sum * 1.0 / size:
            self.targetNode = node
            self.targetAverage = sum * 1.0 / size
        return sum, size
            