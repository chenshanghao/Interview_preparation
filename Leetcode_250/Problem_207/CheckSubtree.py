# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, a, b):
        if not b:
            return True
        return self.dfs(a, b)
        
    def checkTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False
            
        if root1.val != root2.val:
            return False
    
        return self.checkTree(root1.left, root2.left) and self.checkTree(root1.right, root2.right)
        
    def dfs(self, s, t):
        if not s:
            return False
            
        if s.val == t.val and self.checkTree(s, t):
            return True
            
        return self.dfs(s.left, t) or self.dfs(s.right, t)
            
        