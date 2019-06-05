# 先进行一次遍历, 求出每个节点的父节点, 同时找到权值为k的节点.

# 然后再从权值为k的节点进行一次 BFS, 碰到叶子节点直接返回即可. 根据题目要求的优先级顺序, BFS添加后续节点到队列里要按照以下顺序:

# 当前节点的左子节点
# 当前节点的右子节点
# 当前节点的父节点

# Time complexity: O(n)

# Space complexity: O(n)

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
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def findClosestLeaf(self, root, k):
        # Write your code here
        parents = {}
        pValk = self._dfs(root, k, parents)
        q = [pValk]
        vis = [pValk]
        
        while q:
            if not q[0].left and not q[0].right:
                return q[0].val
            if q[0].left and q[0].left not in vis:
                q.append(q[0].left)
                vis.append(q[0])
            if q[0].right and q[0].right not in vis:
                q.append(q[0].right)
                vis.append(q[0])
            if q[0] in parents and parents[q[0]] not in vis:
                q.append(parents[q[0]])
                vis.append(parents[q[0]])
            q.pop(0)
        
        return 0


    def _dfs(self, rt, k, parents):
        res = rt
        tmp = None
        
        if rt.left:
            parents[rt.left] = rt
            tmp = self._dfs(rt.left, k, parents)
            if tmp.val == k:
                res = tmp
        
        if rt.right:
            parents[rt.right] = rt
            tmp = self._dfs(rt.right, k, parents)
            if tmp.val == k:
                res = tmp
        return res