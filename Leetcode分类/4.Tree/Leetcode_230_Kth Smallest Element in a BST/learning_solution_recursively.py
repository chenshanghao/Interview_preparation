# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cnt = []
        self.helper(root, cnt, k)
        return cnt[k - 1]

    def helper(self, node, cnt, k):
        if not node:
            return None
        self.helper(node.left, cnt, k)
        cnt.append(node.val)
        if len(cnt) == k:  # 56 ms  <= 96ms
            return None
        self.helper(node.right, cnt, k)