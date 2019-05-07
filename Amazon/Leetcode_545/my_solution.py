"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        # write your code here
        res = []
        if not root:
            return res
        leftList, rightList, leaveList = [], [], []
        if root.left:
            leftList = self.findLeftBoundary(root.left, [])
        if root.right:
            rightList = self.findRightBounday(root.right, [])
        leaveList = self.findLeaves(root, [])
        
        if leftList and leaveList and leftList[-1] == leaveList[0]:
            leaveList = leaveList[1:]
        rightList = rightList[::-1]  
        if rightList and leaveList and leaveList[-1] == rightList[0]:
            rightList = rightList[1:]
        
        res = [root.val] + leftList + leaveList + rightList

        return res
    
    def findLeftBoundary(self, node, res):
        res.append(node.val)
        if node.left:
            self.findLeftBoundary(node.left, res)
            return res
        if node.right:
            self.findLeftBoundary(node.right, res)
            return res
        return res
    
    def findRightBounday(self, node, res):
        res.append(node.val)
        if node.right:
            self.findRightBounday(node.right, res)
            return res
        if node.left:
            self.findRightBounday(node.left, res)
            return res
        return res
    
    def findLeaves(self, node, res):
        if not node.left and not node.right:
            res.append(node.val)
            return res
        if node.left:
            self.findLeaves(node.left, res)
        if node.right:
            self.findLeaves(node.right, res)
        return res
    
    
            
            
