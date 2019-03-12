# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, float('-inf'), root.val) and self.helper(root.right, root.val, float('inf'))
    
    def helper(self, node, leftMin, rightMax):
        if not node:    return True
        if not(leftMin < node.val < rightMax):  return False
        return self.helper(node.left, leftMin, node.val) and self.helper(node.right, node.val, rightMax )
        