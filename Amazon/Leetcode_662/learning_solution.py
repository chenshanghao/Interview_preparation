"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the maximum width of the given tree
    """
    def widthOfBinaryTree(self, root):
        # Write your code here
        res = 0
        if not root:
            return res
        queue = [(root, 0)]
        while queue:
            left = queue[0][1]
            right = left
            new_queue = []
            for element in queue:
                node, right = element[0], element[1]
                if node.left:
                    new_queue.append((node.left, right * 2))
                if node.right:
                    new_queue.append((node.right, right * 2 + 1))
            res = max(res, right - left + 1)
            queue = new_queue
        return res
                    
                