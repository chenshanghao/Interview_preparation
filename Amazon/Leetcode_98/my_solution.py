"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if not root:
            return True
        return self.checkisValidBST(root, float('-inf'), float('inf'))
        
    def checkisValidBST(self, node, left, right):
        if not node:
            return True
        elif left < node.val < right:
            return self.checkisValidBST(node.left, left, node.val) and self.checkisValidBST(node.right, node.val, right)
        else:
            return False
            
        
