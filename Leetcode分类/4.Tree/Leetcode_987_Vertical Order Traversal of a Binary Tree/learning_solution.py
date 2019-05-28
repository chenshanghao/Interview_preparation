# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        # bfs to set (x,y) to each node
        node_list = []
        q = [(0,0,root)]
        while q:
            x,y,node = q.pop(0)
            node_list.append((x,y,node.val))
            if node.left: q.append((x-1,y-1,node.left))
            if node.right: q.append((x+1,y-1,node.right))
        
        # sort by x then y then val
        node_list = sorted(node_list, key=lambda x:(x[0],-x[1],x[2]))
        
        # combine with same x
        ret = []
        last_x = node_list[0][0]-1
        for x,y,v in node_list:
            if x != last_x:
                ret.append([v])
                last_x = x
            else:
                ret[-1].append(v)
        return ret