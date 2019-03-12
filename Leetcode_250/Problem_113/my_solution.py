# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        if not root:    return self.res
        self.helper(root, [root.val], sum)
        return self.res
        
        
    def helper(self, node, tmp, target):
        if not node.left and not node.right and sum(tmp) == target:
            self.res.append(tmp[:])
            
        if node.left:
            tmp.append(node.left.val)
            self.helper(node.left, tmp, target)
            tmp.pop()
            
        if node.right:
            tmp.append(node.right.val)
            self.helper(node.right, tmp, target)
            tmp.pop()
            