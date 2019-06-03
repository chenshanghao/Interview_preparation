# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        return self.checkValidBST(root.left, float('-inf'), root.val) and self.checkValidBST(root.right, root.val, float('inf'))
        
    def checkValidBST(self, node, l_min, r_max):
        if not node:
            return True
        if l_min < node.val < r_max:
            return self.checkValidBST(node.left, l_min, node.val) and self.checkValidBST(node.right, node.val, r_max)
        return False       