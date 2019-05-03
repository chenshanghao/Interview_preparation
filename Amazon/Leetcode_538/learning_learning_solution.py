"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# 从右子树开始递归，每次加上右子树的和，再递归左子树即可。



class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):
        if root is None:
            return
        if root.right:
            self.helper(root.right)
        
        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.helper(root.left)