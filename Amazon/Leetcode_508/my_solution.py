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
    @return: all the values with the highest frequency in any order
    """
    def findFrequentTreeSum(self, root):
        # Write your code here
        res = []
        if not root:
            return res
        self.maxSum = float('-inf')
        dictSumNum = {}
        self.helper(root, dictSumNum)
        
        for key, val in dictSumNum.items():
            if val == self.maxSum:
                res.append(key)
        return res
        
        
    def helper(self, node, dictSumNum):
        if not node:
            return 0
        nodeSum = node.val + self.helper(node.left, dictSumNum) + self.helper(node.right, dictSumNum)
        if nodeSum not in dictSumNum:
            dictSumNum[nodeSum] = 1
        else:
            dictSumNum[nodeSum] += 1
        self.maxSum = max(self.maxSum, dictSumNum[nodeSum])
        return nodeSum
        