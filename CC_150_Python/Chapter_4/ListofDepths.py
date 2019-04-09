class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def list_of_depths(self, root):
        if not root:
            return []

        depths = []
        q = []
        q.append(root)

        while q:
            parents = q
            depths.append(q)
            q = []

            for parent in parents:
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)
        return depths



