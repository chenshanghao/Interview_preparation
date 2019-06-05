"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: Whether it is a full tree
    """
    def isFullTree(self, root):
        # write your code here
        return self.helper(root)
    
    def helper(self, node):
        if not node:
            return True
        elif not node.left and not node.right:
            return True
        elif node.left and not node.right:
            return False
        elif node.right and not node.left:
            return False
        else:
            return self.helper(node.left) and self.helper(node.right)