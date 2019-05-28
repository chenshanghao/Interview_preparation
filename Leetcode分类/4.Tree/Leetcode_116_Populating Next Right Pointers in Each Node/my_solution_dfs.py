"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        stack = [root]
        while stack:
            newStack = []
            stackLength = len(stack)
            for index, node in enumerate(stack):
                if node.left:   newStack.append(node.left)
                if node.right:  newStack.append(node.right)
                if index < stackLength - 1:
                    node.next = stack[index+1]
            stack = newStack 
        return root        
        