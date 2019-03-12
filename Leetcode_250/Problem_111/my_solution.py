# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        min_depth = 1
        while stack:
            new_stack = []
            for node in stack:
                if not node.left and not node.right:    return min_depth
                if node.left:   new_stack.append(node.left)
                if node.right:  new_stack.append(node.right)
            min_depth += 1
            stack = new_stack
        return min_depth
                
                
            
        