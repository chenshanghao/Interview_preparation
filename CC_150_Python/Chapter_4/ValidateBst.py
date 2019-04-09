# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
        
    def helper(self, node, left, right):
        if not node:
            return True
        if left < node.val < right:
            return self.helper(node.left, left, node.val) and self.helper(node.right, node.val, right)
        else:
            return False