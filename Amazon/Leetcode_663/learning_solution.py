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
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        # write your code here
        sumChildTree = []
        sumRootTree = self.helper(root, sumChildTree)
        
        if sumRootTree // 2 in sumChildTree[:len(sumChildTree)-1]:
            return True
        else:
            return False
        
    def helper(self, node, sumChildTree):
        if not node:
            return 0
        sumTree = node.val + self.helper(node.left, sumChildTree) + self.helper(node.right, sumChildTree)
        sumChildTree.append(sumTree)
        return sumTree
        
    

        # def sum_(node):
        #     if not node: return 0
        #     seen.append(sum_(node.left) + sum_(node.right) + node.val)
        #     return seen[-1]
        # total = sum_(root)
        # print(seen)
        # seen.pop()
        # return total / 2.0 in seen