# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != -1
        
        
    def helper(self, node):
        if not node:
            return 0
        left_depth = self.helper(node.left) + 1
        right_depth = self.helper(node.right) + 1
        if left_depth > 0 and right_depth > 0 and abs(right_depth - left_depth) <= 1:
            return max(right_depth, left_depth)
        else:
            return -1
            
        
        
        