"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            new_stack = []
            levelValue = []
            for node in stack:
                levelValue.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            res.append(levelValue)
            stack = new_stack
        return res
                
