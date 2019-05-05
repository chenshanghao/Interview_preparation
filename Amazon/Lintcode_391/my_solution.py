"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        takeoff = sorted([i.start for i in airplanes])
        land = sorted([i.end for i in airplanes ])
        res = 0
        cnt = 0
        i, j = 0, 0
        while( i < len(takeoff) and j < len(land)):
            if takeoff[i] < land[j]:
                i += 1
                cnt += 1
                res = max(res, cnt)
            else:
                cnt -= 1
                j += 1
        return res
            
        
        
        
