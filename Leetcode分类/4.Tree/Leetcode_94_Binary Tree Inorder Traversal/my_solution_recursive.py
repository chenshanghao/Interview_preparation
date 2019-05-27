"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        res = []
        self.treeInorderTraversal(root, res)
        return res
    
    def treeInorderTraversal(self, node, res):
        if not node:
            return
        if node.left:
            self.treeInorderTraversal(node.left, res)
        res.append(node.val)
        if node.right:
            self.treeInorderTraversal(node.right, res)