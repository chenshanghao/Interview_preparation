# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.treePreorderTraversal(root, res)
        return res
    
    def treePreorderTraversal(self, node, res):
        if node:
            res.append(node.val)
            self.treePreorderTraversal(node.left, res)
            self.treePreorderTraversal(node.right, res)
        return
        
        