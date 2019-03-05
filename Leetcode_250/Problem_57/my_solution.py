# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        index = len(intervals)
        for i in range(len(intervals)):
            if newInterval.start < intervals[i].start:
                index = i
                break
        intervals.insert(index, newInterval)
        res = []
        for inter in intervals:
            if not res or res[-1].end< inter.start:
                res.append(inter)
            else:
                res[-1].end = max(res[-1].end, inter.end)
        return res
        