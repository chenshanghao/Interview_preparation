# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        return self.dfs(root, sum, 0)
    
    def dfs(self, node, sum, sumVal):
        sumVal = sumVal + node.val
        if not node.left and not node.right:
            return sumVal == sum
        leftPathSum, rightPathSum = False, False
        if node.left:
            leftPathSum = self.dfs(node.left, sum, sumVal)
        if node.right:
            rightPathSum = self.dfs(node.right, sum, sumVal)
        return leftPathSum or rightPathSum
        