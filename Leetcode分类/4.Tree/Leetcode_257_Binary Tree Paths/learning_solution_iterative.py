# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res, queue = [], [(root, "")]
        while queue:
            node, ls = queue.pop(0)
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.left:
                queue.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                queue.append((node.right, ls + str(node.val) + "->"))
        return res