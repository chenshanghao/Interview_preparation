class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        res = []
        if not root:
            return res
        stack = [root]
        node = None
        
        while stack or node:
            if not node:
                node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            node = node.left
        return res