# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        # stack used to hold the matching pairs
        stack = []
        # if root=None, or if root has no children, root is symmetric
        if not root or (not root.left and not root.right):
            return True
        
        stack.append((root.left, root.right))
        while len(stack):
            # the order of node retrieval matters little here, because we only care about
            # pair content and not the relative order of different pairs; queue is quicker
            # at finding shallow discrepancy, where stack is quicker at finding deeper
            # discrepancy
            left, right = stack.pop()
            # if left and right are not symmetric, return false
            if not left or not right or (left.val != right.val):
                return False
            # only append if the corresponding pairs exist
            if left.left or right.right:
                stack.append((left.left, right.right))
            if left.right or right.left:
                stack.append((left.right, right.left))
        return True
        