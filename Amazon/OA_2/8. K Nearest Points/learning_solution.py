"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq
from heapq import heappush, heappop, nlargest, nsmallest
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        
        dis = []
        for p in points:
            d = (p.x - origin.x) ** 2  + (p.y - origin.y) ** 2
            dis.append(((d, p.x, p.y), p))
        heapq.heapify(dis)
        res_list = heapq.nsmallest(k, dis)
        res = []
        for (dis, p) in res_list:
            res.append(p)
        return res
        
