# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.dfs(root, sum, [], res,)
        return res
        
    def dfs(self, node, sum, path, res):
        path.append(node.val)
        if node.val == sum and not node.left and not node.right:
            res.append(path)
        if node.left:
            leftPath = path[:]
            self.dfs(node.left, sum - node.val, leftPath, res,)
        if node.right:
            rightPath = path[:]
            self.dfs(node.right, sum - node.val, path[:], res)
        